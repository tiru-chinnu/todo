from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__, template_folder="templates")

todos = [
    {"done": False, "task": "make a todo list using flask "},
    {"done": False, "task": "compliting portfolio"},
]


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run(debug=True)
