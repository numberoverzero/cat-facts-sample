<!DOCTYPE HTML>
<html>
  <head>
    <title>{{title or 'No title'}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="/cats.css">
  </head>
  <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">Andy's Team</a>
    </div>
    <div class="collapse navbar-collapse navbar-ex8-collapse">
      <ul class="nav navbar-nav">
      %for header, url in nav:
        %if header == current_nav:
        <li class="active"><a href="{{url}}">{{header}}</a></li>
        %else:
        <li><a href="{{url}}">{{header}}</a></li>
        %end
      %end
      </ul>
    </div>
  </nav>
  <body>
    %include
  </body>
</html>
