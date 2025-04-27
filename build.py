
INDEX_TEMPLATE="""
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>

  <body>
    <div id="main">
      <h1 id="title">Hadleys Blog</h1>

      #ARTICLES
    <div>
  </body>
</html>
"""

def generate_article_div(url: str, title: str) -> str:
    return f"""
<div class=\"blog-item\">
    <a class=\"blog-title\" href=\"{url}\">{title}<a>
</div>
"""

def main():
    articles = ""

    articles += generate_article_div("test", "test");

    html = INDEX_TEMPLATE
    html.replace("#ARTICLES", articles)

main()
