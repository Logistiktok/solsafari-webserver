from flask import Flask
from flask import request
from flask import render_template


hits = 0

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ajax/', methods=['GET', 'POST'])
def ajax():
    global hits
    return str(hits)

@app.route('/client/')
def client():
    return render_template('client.html')


@app.route('/client')
def client3():
    return render_template('client.html')

@app.route('/point/', methods=['GET', 'POST'])
def point():
    global hits
    if request.method == 'POST':
        req = request.get_json()
        hits = hits + req["hits"]
        print(hits)
        return "OK"
    else:
        point = 0
        return render_template('point.html', point=hits)