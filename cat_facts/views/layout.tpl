<!DOCTYPE HTML>
<html>
  <head>
    <title>{{title or 'No title'}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/normalize.css">
    <link rel="stylesheet" href="/gridism.css">
    <link rel="stylesheet" href="/cats.css">
  </head>
  <body class="wrap">
    <header>
      <div class="grid">
        <div class="unit one-third center-on-mobiles">
          <h1><a href="/">Andy's Team</a></h1>
        </div>
        <nav class="unit two-thirds align-right center-on-mobiles">
            <ul class="header-nav">
              <li><a href="/facts">Facts</i></a></li>
              <li><a href="/stats">Stats</i></a></li>
            </ul>
        </nav>
      </div>
    </header>
    <div class="content grid unit whole">
      %include
    </div>
    <footer>
      <div class="unit whole align-center">
        <p>
          Served from <strong>{{host}}</strong>
        </p>
      </div>
    </footer>
  </body>
</html>
