import os
import re

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
    return f"""<div class=\"blog-item\">
        <a class=\"blog-title\" href=\"{url}\">{title}<a>
      </div>"""

def main():
    articles = ""

    for file in os.listdir("blogs"):
        fullpath = f"blogs/{file}"
        with open(fullpath) as f:
            data = f.read();

            title = re.findall(r'id=["\']title["\'][^>]*>(.*?)</', data)[0]

            articles += generate_article_div(fullpath, title);

    html = INDEX_TEMPLATE
    html = html.replace("#ARTICLES", articles)

    print(html)

    with open("index.html", "w+") as f:
        f.write(html)

main()
