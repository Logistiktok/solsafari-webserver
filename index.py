from flask import Flask
from flask import request
from flask import render_template


hits = 0

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/point/', methods=['GET', 'POST'])
def point():
    if request.method == 'POST':
        req = request.get_json()
        print(req["hits"])
        return "Tak for point"
    else:
        point = 0
        return render_template('point.html', point=point)