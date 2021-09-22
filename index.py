from datetime import time
from flask import Flask
from flask import request
from flask import render_template
from flask import Response
import json


orangeHits = 0
blueHits = 0
rounds = []
point = 0
current_round_number = 1
is_paused_state = False


app = Flask(__name__)
sock = Sock(app)
app.url_map.strict_slashes = False #Fixes trailing slashes so they are redicrected


@app.route('/')
def hello_world():
    return 'Gå til /app for at finde applicationen!'


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    global point, rounds, current_round_number, orangeHits, blueHits
    current_round_number += 1
    rounds.append({"blueHits": blueHits, "orangeHits": orangeHits})
    blueHits = 0
    orangeHits = 0
    return "Ok"

@app.route('/ajax', methods=['GET', 'POST'])
def ajax():
    global orangeHits, blueHits, current_round_number
    data = {"blueHits": blueHits, "orangeHits": orangeHits, "rounds": current_round_number, "state": is_paused_state}
    return Response(json.dumps(data),  mimetype='application/json')

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


@app.route('/app')
def client():
    global current_round_number
    return render_template('client.html', index_number=current_round_number, orange_hits=orangeHits, blue_hits=blueHits, point=point, state=is_paused_state)


@app.route('/point', methods=['GET', 'POST'])
def assig_points():
    print(request.get_json())
    global blueHits, orangeHits
    if request.method == 'POST':
        json = request.get_json()
        if not is_paused_state:
            blueHitsJson = round(json["blueHits"]/2) #THe targets counts one hot twice beceuse hardware. The actual hits  is therefore counted / 2
            orangeHitsJson = round(json["orangeHits"]/2)
            blueHits = blueHits + blueHitsJson
            orangeHits = orangeHits + orangeHitsJson
        #print("blueHits" + str(blueHits))
        #print("orangeHits" + str(orangeHits))
        return "OK"
    else:
        return render_template('point.html', point=point)
