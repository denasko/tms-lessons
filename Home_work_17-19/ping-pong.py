from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_home_page():
    return f"""
<html>
    <head>
        <meta charset="UTF-8">
        <hr>
            <title>Ping-Pong</title>
    </head>
    <body>
        <h1 align="center"><a href='/ping'> Start <a/> </h1>      
        <hr>
    </body>
</html>
"""


@app.route('/ping')
def show_ping_page():
    return f"""
    <html>
        <head>
            <meta charset="UTF-8">
                <title>Ping-Pong</title>
        </head>
        <body>
            <h1 align="center"><a href='/pong'> Ping <a/> </h1>      
            <hr>
            <h3 align="center"><a href='/'> go main page <a/> </h3> 
        </body>
    </html>
    """


@app.route('/pong')
def show_pong_page():
    return f"""
<html>
    <head>
        <meta charset="UTF-8">
            <title>Ping-Pong</title>
    </head>
    <body>
        <h1 align="center"><a href='/ping'> Pong <a/> </h1>      
        <hr>
        <h3 align="center"><a href='/'> go main page <a/> </h3>
    </body>
</html>
"""


if __name__ == '__main__':
    app.run(port=8082, debug=True)
