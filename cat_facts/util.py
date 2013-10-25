import os
import urllib2

_root = None

def set_root(file):
    '''
Pass in __file__ from a script to set that script's directory as the root for
determining absolute paths to resources
'''
    global _root
    _root = os.path.dirname(os.path.realpath(file))

def get_root():
    return _root

def abs_path(filename):
    '''Absolute path from _root '''
    if not _root:
        raise ValueError("Unknown root. Use set_root(__file__) from a script in the root directory first.")
    return os.path.join(_root, filename)

def list_files(dir):
    '''List files in a directory.
    Not recursive, excludes folders.'''
    root = abs_path(dir)
    contents = os.listdir(root)
    is_file = lambda filename: os.path.isfile(os.path.join(root, filename))
    return filter(is_file, contents)

def load_file(filename):
    '''Returns the contents of the given file in the data folder.'''
    path = abs_path(filename)
    with open(path) as f:
        data = f.read()
        return sanitize(data)

def load_file_config(config, filename):
    '''key = value in filename becomes config[key] = value'''
    config_lines = load_file(filename).split(u'\n')
    for line in config_lines:
        line = until(line, u'#')
        if not line or u'=' not in line:
            continue
        key, value = line.split(u'=', 1)
        key, value = key.strip(), value.strip()
        value = type_coerce(value)
        config[key] = value
    return config

def load_env_config(config, keys, overwrite_null=False):
    '''
    Load environment variables into config, where keys is an iterable of env keys to look up.
    overwrite_null=True means keys not found in env vars are set in config as None. Otherwise, those values aren't set.
    '''
    for key in keys:
        value = os.getenv(key, None)
        if value is not None or overwrite_null:
            config[key] = value
    return config

def sanitize(string):
    '''Returns the string as unicode, with \n line endings'''
    if string is None:
        return u''
    try:
        string = unicode(string, encoding='utf-8')
    # Already unicode
    except (UnicodeEncodeError, TypeError):
        pass
    string = string.replace(u'\r\n', u'\n')
    return string

def type_coerce(value):
    '''
    values can have a type appended, such as $int
    if a valid type is appended, coerces the value to that type.
    otherwise, returns the value
    '''
    type_map = {
        'int': int,
        'float': float,
        'bool': bool,
    }
    for type in type_map:
        suffix = '$' + type
        if value.endswith(suffix):
            value = until(value, suffix).strip()
            return type_map[type](value)
    return value

def until(string, suffix):
    '''Returns the string until the first occurance of suffix'''
    if not suffix:
        return string
    return string.split(suffix, 1)[0]

def load_url(url):
    try:
        return urllib2.urlopen(url).read()
    except urllib2.URLError:
        return ""
