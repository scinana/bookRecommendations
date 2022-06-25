from flask import Flask, render_template
import books

app = Flask(__name__)


@app.route("/")
def index():
    gjson = books.graph_bubbles()
    return render_template("index.html", gjson=gjson)
