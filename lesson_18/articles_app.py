import dataclasses
import sqlite3

from flask import Flask, abort, request, redirect, session

from flask_session import Session


@dataclasses.dataclass
class Article:
    id: int
    title: str
    text: str
    author: str
    like_count: int


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


def get_all_articles() -> list[Article]:
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.execute("""SELECT id,title,text,author,like_count FROM articles""")
        result = []
        for i in cur.fetchall():
            result.append(Article(id=i[0], title=i[1], text=i[2], author=i[3], like_count=i[4]))
            # result = [Article(*i) for i in cur.fetchall()]
        return result


def get_article(article_id: int, flag_raise=True) -> Article | None:
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.execute("""SELECT id,title,text,author,like_count FROM articles WHERE id=?""", [article_id])
    result = cur.fetchone()
    if result:
        return Article(id=result[0], title=result[1], text=result[2], author=result[3], like_count=result[4])
    elif flag_raise is False:
        return None
    raise ValueError(f'Article with ID = {article_id}  not found')


def save_article(article: Article):
    with sqlite3.connect('my_database.db') as conn:
        data = (article.title, article.text, article.author, article.like_count, article.id)
        conn.execute('UPDATE article '
                     'SET title = ?, text = ?, author = ? ,like_count = ?'
                     'WHERE id = ?', (data,))


def plus_minus_like(article_id: int, operation: str):
    with sqlite3.connect('my_database.db') as conn:
        conn.execute(f"""UPDATE articles set like_count=like_count{operation}1 WHERE id=?""", [article_id, ])


@app.route('/articles')
@app.route('/')
def show_home_page():
    articles = get_all_articles()
    articles_html = '\n'.join(
        f"<li><u><a href='/article/{article.id}'>{article.title}</a></li>"
        for article in articles)
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


@app.route('/article/<int:article_id>')
def show_article_id(article_id: int):
    article = get_article(article_id, flag_raise=False)
    if article is None:
        abort(404, 'Article not found')
    return f"""
    <html>
        <head>
            <meta charset="UTF-8">
                <title>Articles APP</title>
        </head>
        <body>
            <a href='/articles'>Go to home page</a>
            <h1 align="center"> {article.title.title()} </h1>
            <h3> Author: {article.author.title()} </h3>      
            <ul type=square> 
            <p>{article.text.title()}</p>  
            </ul>
            <hr>
            <form action="/article/like" method="post">
            <input type="hidden" name="article_id" value="{article.id}"/>
           <input type="submit" value="Like: {article.like_count}"/>
       </form>
        </body>
    </html>
    """


@app.route('/article/like', methods=['POST'])
def like_article():
    article_id = int(request.form['article_id'])
    if session['like'] == 1:
        session['like'] = 0
        plus_minus_like(article_id, '-')
        return redirect(f'/article/{article_id}')
    else:
        session['like'] = 1
        plus_minus_like(article_id, '+')
        return redirect(f'/article/{article_id}')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
