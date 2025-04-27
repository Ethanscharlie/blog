import os
import re

MAIN_SITE_URL = "https://ethanscharlie.github.io/blog/"
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
RSS_TEMPLATE="""
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>Hadley's Blog</title>
  <link>https://ethanscharlie.github.io/</link>
  <description>Yup</description>
  #ARTICLES
</channel>

</rss> 
"""

def generate_article_div(url: str, title: str, desc: str) -> str:
    return f"""<div class=\"blog-item\">
        <a class=\"blog-title\" href=\"{url}\">{title}<a>
        <p class=\"blog-desc\">{desc}</p>
      </div>"""

def generate_article_rss(url: str, title: str, desc: str) -> str:
    return f"""
  <item>
    <title>{title}</title>
    <link>{MAIN_SITE_URL}{url}</link>
    <description>{desc}</description>
  </item>
    """

def main():
    articles = ""
    rss_articles = ""

    for file in os.listdir("blogs"):
        fullpath = f"blogs/{file}"
        with open(fullpath) as f:
            data = f.read();

            title = re.findall(r'id=["\']title["\'][^>]*>(.*?)</', data)[0]
            desc = re.findall(r'id=["\']desc["\'][^>]*>(.*?)</', data)[0]

            articles += generate_article_div(fullpath, title, desc);
            rss_articles += generate_article_rss(fullpath, title, desc);

    html = INDEX_TEMPLATE.replace("#ARTICLES", articles)
    rss = RSS_TEMPLATE.replace("#ARTICLES", rss_articles)

    print("Writing to files...")

    with open("index.html", "w+") as f:
        f.write(html)

    with open("rss", "w+") as f:
        f.write(rss)

main()
