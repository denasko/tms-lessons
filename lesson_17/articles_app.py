import dataclasses
import sqlite3

from flask import Flask


@dataclasses.dataclass
class Article:
    id: int
    title: str
    text: str
    author: str


def get_all_articles() -> list[Article]:
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.execute("""SELECT id,title,text,author FROM articles""")
        result = []
        for i in cur.fetchall():
            result.append(Article(id=i[0], title=i[1], text=i[2], author=i[3]))
            # result = [Article(*i) for i in cur.fetchall()]
        return result


def get_article(article_id: int) -> Article:
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.execute("""SELECT id,title,text,author FROM articles WHERE id=?""", [article_id])
    result = cur.fetchone()
    if result:
        return Article(id=result[0], title=result[1], text=result[2], author=result[3])
    raise ValueError(f'Article with ID = {article_id}  not found')


def save_article(obj: Article):
    with sqlite3.connect('my_database.db') as conn:
        conn.execute("""UPDATE id,title,text,author FROM articles WHERE id=1""",
                     [obj.id, obj.title, obj.text, obj.title])


app = Flask(__name__)


# @app.route('/<string:name>')
# def show_name(name: str):
#     return f'<p>Hello, {name.upper()}!</p>'


@app.route('/articles')
@app.route('/')
def show_home_page():
    articles = get_all_articles()
    articles_html = '\n'.join(
        f'<li><u>{i.title}</li>'
        for i in articles)

    return f"""
<html>
    <head>
        <meta charset="UTF-8">
            <title>Articles APP</title>
    </head>
    <body>
        <h1 align="center"> All Articles </h1>      
        <ul type=square> 
        {articles_html}    
        </ul>
        <hr>
    </body>
</html>
"""


if __name__ == '__main__':
    app.run(port=8080, debug=True)
