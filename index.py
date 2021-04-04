from flask import Flask
from flask import request
from flask import render_template
from flask import Response
import json


hits = 0
rounds = []


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ajax/', methods=['GET', 'POST'])
def ajax():
    global hits
    return str(hits)

@app.route('/reset/', methods=['GET', 'POST'])
def reset():
    global hits
    global rounds
    rounds.append(hits)
    hits = 0
    return "Ok"

@app.route('/rounds/', methods=['POST'])
def save_rounds():
    global rounds
    print(rounds)

    dict = {"rounds": rounds}
    return Response(json.dumps(dict),  mimetype='application/json')

@app.route('/client/')
def client():
    return render_template('client.html')


@app.route('/client')
def client2():
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