from flask import Flask
from flask import request
from flask import render_template
from flask import Response
import json


point = 0
rounds = []
current_round_number = 1;
is_paused_state = False;


app = Flask(__name__)
app.url_map.strict_slashes = False #Fixes trailing slashes so they are redicrected


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ajax', methods=['GET', 'POST'])
def ajax():
    global point, current_round_number
    data = {"point": point, "rounds": current_round_number, "state": is_paused_state}
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    global point, rounds, current_round_number
    current_round_number += 1
    rounds.append(point)
    point = 0
    return "Ok"

@app.route('/rounds', methods=['POST'])
def save_rounds():
    global rounds
    print(rounds)
    dict = {"rounds": rounds}
    return Response(json.dumps(dict),  mimetype='application/json')

@app.route('/statechange', methods=['POST'])
def statechange():
    global is_paused_state
    json_data = request.get_json()
    state = json_data['state']
    is_paused_state = state
    return "ok"

@app.route('/client')
def client():
    global current_round_number
    return render_template('client.html', index_number=current_round_number, point=point, state=is_paused_state)


@app.route('/point', methods=['GET', 'POST'])
def assig_points():
    global point
    if request.method == 'POST':
        req = request.get_json()
        if not is_paused_state:
            point = point + req["hits"]
        print(point)
        return "OK"
    else:
        point = 0
        return render_template('point.html', point=point)
