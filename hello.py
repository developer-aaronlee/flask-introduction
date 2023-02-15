from flask import Flask

app = Flask(__name__)


# def make_bold(func):
#
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         new_text = f"<b>{text}</b>"
#         return new_text
#
#     return wrapper

def make_bold(func):

    def wrapper():
        return "<b>" + func() + "</b>"

    return wrapper


def make_emphasis(func):

    def wrapper():
        return "<em>" + func() + "</em>"

    return wrapper


def make_underline(func):

    def wrapper():
        return "<u>" + func() + "</u>"

    return wrapper


@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
           "<p>This is a paragraph!</p>" \
           "<img src='https://media2.giphy.com/media/LPlmexh8SLjO9OwPxP/giphy.webp?" \
           "cid=ecf05e47uzac02r86zcpox84nqnzrfy5dmwd58yqf13ccu0h&rid=giphy.webp&ct=g' width=200>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "<p>Bye!</p>"


# @app.route("/username/<name>")
# def greet(name):
#     return f"hello {name}!"


# @app.route("/username/<path:name>")
# def greet(name):
#     return f"hello {name}!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello {name}! you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)