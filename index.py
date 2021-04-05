from flask import Flask
from flask import request
from flask import render_template
from flask import Response
import json


point = 0
rounds = []
current_round_number = 1;


app = Flask(__name__)
app.url_map.strict_slashes = False #Fixes trailing slashes so they are redicrected


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ajax', methods=['GET', 'POST'])
def ajax():
    global point
    return str(point)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    global point
    global rounds
    global current_round_number
    current_round_number += current_round_number
    rounds.append(point)
    point = 0
    return "Ok"

@app.route('/rounds', methods=['POST'])
def save_rounds():
    global rounds
    print(rounds)
    dict = {"rounds": rounds}
    return Response(json.dumps(dict),  mimetype='application/json')

@app.route('/client')
def client():
    global current_round_number
    return render_template('client.html', index_number=current_round_number, point=point)


@app.route('/point', methods=['GET', 'POST'])
def assig_points():
    global point
    if request.method == 'POST':
        req = request.get_json()
        point = point + req["hits"]
        print(point)
        return "OK"
    else:
        point = 0
        return render_template('point.html', point=point)
