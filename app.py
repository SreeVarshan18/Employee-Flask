from flask import Flask, render_template

App = Flask(__name__)


@App.route("/")
def home():
    return render_template("home.html")

@App.route("/search")
def search():
    return render_template("search.html")

@App.route("/update")
def update():
    return render_template("update.html")


@App.route("/delete")
def delete():
    return render_template("delete.html")



if __name__ == "__main__":
    App.run()