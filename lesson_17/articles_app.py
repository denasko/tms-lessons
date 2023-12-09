import sqlite3
from dataclasses import dataclass

from flask import Flask, abort, request, redirect, session, render_template, url_for, flash

from flask_session import Session


@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str
    like_count: int


@dataclass
class User:
    id: int
    user_name: str
    password: str


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
        conn.execute('UPDATE articles '
                     'SET title = ?, text = ?, author = ? ,like_count = ?'
                     'WHERE id = ?', data)


def check_user(login: 'User.user_name', ps: 'User.password') -> User | None:
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.execute("""SELECT id,user_name,password FROM user WHERE user_name=? AND password=?""", (login, ps))
    data = cur.fetchone()
    if data:
        return User(id=data[0], user_name=data[1], password=data[2])
    return None


def create_user(login: 'User.user_name', ps: 'User.password') -> 'User.user_name':
    with sqlite3.connect('my_database.db') as conn:
        conn.execute(f"""INSERT INTO user (user_name,password)
                    VALUES(?,?)""", (login, ps))
    return login


@app.route('/')
@app.route('/articles')
def show_home_page():
    articles = get_all_articles()
    return render_template('home_page.html', articles=articles)


@app.route('/article/<int:article_id>')
def show_article_id(article_id: int):
    article = get_article(article_id, flag_raise=False)
    if article is None:
        abort(404, 'Article not found')
    return render_template('article_page.html', article=article)


@app.route('/article/like', methods=['POST'])
def like_article():
    article_id = int(request.form['article_id'])
    article = get_article(article_id, flag_raise=False)
    liked_products = session.setdefault('article_id', set())
    if session['is_auth'] == True:
        if article_id in liked_products:
            article.like_count -= 1
            liked_products.remove(article_id)
        else:
            article.like_count += 1
            liked_products.add(article_id)
        save_article(article)
        return redirect(f'/article/{article_id}')
    flash('In order to like you need to log in to your account.')
    return redirect(url_for('show_home_page'))


@app.route('/login')
def show_login_to_account_page():
    return render_template('login_page.html')


@app.route('/login', methods=['POST'])
def login_to_account():
    login = request.form['login']
    password = request.form['password']
    user = check_user(login, password)
    print('chek user')
    if user:
        session['is_auth'] = True
        flash(f'Hello {user.user_name.title()}!')
        return redirect(url_for('show_home_page'))
    flash('You entered incorrect data!')
    return redirect(url_for('show_login_to_account_page'))


@app.route('/auth')
def show_auth_page():
    return render_template('auth_page.html')


@app.route('/auth', methods=['POST'])
def auth_new_user():
    login = request.form['login']
    password = request.form['password']
    if len(login) > 4 and len(password) > 4:
        user_name = create_user(login, password)
        print('create user')
        session['is_auth'] = True
        flash(f'Congratulations on registering, {user_name.title()}!')
        return redirect(url_for('show_home_page'))
    flash('Login and password must be more than 4 characters!')
    return redirect(url_for('show_auth_page'))


@app.route('/logout')
def logout():
    session['is_auth'] = False
    flash('Goodbye :(')
    return redirect(url_for('show_home_page'))


if __name__ == '__main__':
    app.run(port=8080, debug=True)
