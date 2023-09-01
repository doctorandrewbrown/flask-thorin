import os
from flask import Flask, render_template


app = Flask(__name__)

# define "views" ie functions to run when triggered by given route
@app.route("/")
def index():
    return render_template("index.html", title = "Home", list=["andy", "david", "brown"])


@app.route("/about")
def about():
    return render_template("about.html", title = "Test")


@app.route("/contact")
def contact():
    return render_template("contact.html", title = "Call me")

@app.route("/post")
def post():
    return render_template("post.html", title = "Test Post")

# test route for dynamic url
@app.route("/about/<name>")
def say_hello(name):
    return render_template("say_hello.html", title = f"Hello {name}")


if __name__ == "__main__":
    # PORT is needed for heroku deploy
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)