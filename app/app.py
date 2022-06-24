from flask import Flask, render_template
import books

app = Flask(__name__)

@app.route('/')
def index():
    gjson = books.graphBubbles()
    template = render_template('index.html', graphJson=gjson)
    print(template)
    return template
