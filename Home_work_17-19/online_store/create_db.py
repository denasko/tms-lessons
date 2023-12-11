import sqlite3
from dataclasses import dataclass

from flask import Flask, abort, render_template, session, request, redirect, flash, url_for

from flask_session import Session

PATH = 'store.db'
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Product:
    id: int
    name: str
    description: str
    category_id: str
    like_count: int


@dataclass
class User:
    id: int
    login: str
    password: str


def load_product(product_name: str, flag_raise=True) -> Product | None:
    with sqlite3.connect(PATH) as conn:
        cur = conn.execute("""SELECT * FROM product WHERE name=?""", (product_name,))
        result = cur.fetchone()
        if result:
            return Product(id=result[0], name=result[1], description=result[2], category_id=result[3],
                           like_count=result[4])
        elif flag_raise is False:
            return None
        raise ValueError(f'Article with ID = {product_name}  not found')


def save_product(product: Product):
    with sqlite3.connect(PATH) as conn:
        conn.execute('UPDATE product '
                     'SET name = ?, description = ?, category_id = ? ,like_count = ?'
                     'WHERE name = ?',
                     (product.name, product.description, product.category_id, product.like_count, product.name))


def load_product_category(category_name: str) -> list:
    with sqlite3.connect(PATH) as conn:
        cur = conn.execute("""SELECT product.id,product.name,product.description,product.category_id,
                        product.like_count,category.name
                        FROM category JOIN product
                        on category.id=product.category_id
                        where category.name=?""", (category_name,))
        result = []
        for i in cur.fetchall():
            result.append(Product(id=i[0], name=i[1], description=i[2], category_id=i[3], like_count=i[4]))
        category_name = i[5]
        result.append(category_name)
    return result


def get_category_name(product_name: 'Product.name')->tuple:
    with sqlite3.connect(PATH) as conn:
        category_name = conn.execute("""SELECT DISTINCT category.name
                                    FROM category JOIN product
                                    on category.id=product.category_id
                                    where product.name=?""", (product_name,))
        return category_name.fetchone()


def get_list_category() -> list[tuple]:
    with sqlite3.connect(PATH) as conn:
        cur = conn.execute(
            """SELECT category.name,product.name,product.category_id FROM product JOIN category ON 
            product.category_id=category.id""")
        data = cur.fetchall()
        return data


@app.route('/')
@app.route('/my_store')
def show_home_page():
    data = get_list_category()
    return render_template('main_page.html', menu=['Authorization', 'Login'], data=data,
                           auth=session['is_auth'])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html', menu=['Authorization', 'Login'], auth=session['is_auth'],
                           title='Page not found')


@app.route('/product/<path:product_name>')
def show_product_id(product_name: 'Product.name'):
    product = load_product(product_name, flag_raise=False)
    if product is None:
        abort(404, 'Article not found')
    category_name = get_category_name(product_name)
    return render_template('product_page.html', product=product, category_name=category_name,
                           auth=session['is_auth'], title=product.name, menu=['Authorization', 'Login'])


@app.route('/favorites')
def show_favorite_product():
    all_product = []
    if session['fovorite_product']:
        for i in session.get('fovorite_product'):
            all_product.append(load_product(i))
        return render_template('favorites_product.html', products_html=all_product,
                               auth=session['is_auth'], title='All favorite products', menu=['Authorization', 'Login'])
    flash("There's nothing here")
    return render_template('favorites_product.html', auth=session['is_auth'],
                           title='All favorite products', menu=['Authorization', 'Login'])


@app.route('/category/<category_name>')
def show_category(category_name: str):
    category = category_name
    products = load_product_category(category)
    category_name = products.pop()
    return render_template('category.html', products=products, auth=session['is_auth'],
                           title=category_name, menu=['Authorization', 'Login'])


@app.route('/product/like', methods=['POST'])
def like_product():
    product_name = str(request.form['product_name'])
    product = load_product(product_name)
    liked_products = session.setdefault('liked_articles', set())
    if session['is_auth']:
        if product_name in liked_products:
            product.like_count -= 1
            liked_products.remove(product_name)
        else:
            product.like_count += 1
            liked_products.add(product_name)
        save_product(product)
        return redirect(url_for('show_product_id', product_name=product_name))
    flash('In order to like you need to log in to your account.')
    return redirect(url_for('show_home_page'))


@app.route('/product/favorites', methods=['POST'])
def favor_product():
    product_name = str(request.form['product_name'])
    product = load_product(product_name)
    favorites_products = session.setdefault('fovorite_product', set())
    if product_name in favorites_products:
        favorites_products.remove(product_name)
        flash('Product removed from favorites ')
    else:
        favorites_products.add(product_name)
        flash('Product added from favorites ')
    save_product(product)
    return redirect(
        url_for('show_product_id', product_name=product_name, menu=['Authorization', 'Login'], auth=session['is_auth']))


# ----------------------------------------REGISTRATION-------------------------------------------------------


def check_user(login: 'User.login', ps: 'User.password') -> User | None:
    with sqlite3.connect(PATH) as conn:
        cur = conn.execute("""SELECT id,login,password FROM user WHERE login=? AND password=?""",
                           (login, ps))
    data = cur.fetchone()
    if data:
        return User(id=data[0], login=data[1], password=data[2])
    return None


def create_user(login: 'User.login', ps: 'User.password') -> 'User.login':
    with sqlite3.connect(PATH) as conn:
        conn.execute(f"""INSERT INTO user (login,password)
                    VALUES(?,?)""", (login, ps))
    return login


@app.route('/login')
def show_login_to_account_page():
    return render_template('login_page.html', auth=session['is_auth'], title='Login to account',
                           menu=['Authorization', 'Login'])


@app.route('/login', methods=['POST'])
def login_to_account():
    login = request.form['login']
    password = request.form['password']
    user = check_user(login, password)
    if user:
        session['is_auth'] = login
        flash(f'Hello {user.login.title()}!')
        return redirect(url_for('show_home_page'))
    flash('You entered incorrect data!')
    return redirect(url_for('show_login_to_account_page'))


@app.route('/authorization')
def show_auth_page():
    return render_template('auth_page.html', menu=['Authorization', 'Login'], auth=session['is_auth'],
                           title='Create a new account')


@app.route('/authorization', methods=['POST'])
def auth_new_user():
    login = request.form['login']
    password = request.form['password']
    if len(login) > 4 and len(password) > 4:
        user_name = create_user(login, password)
        session['is_auth'] = login
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
