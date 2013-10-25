from cat_facts import app

if app.config['MODE'] == 'DASHBOARD':
    import dashboard_views
else:
    import server_views
