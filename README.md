The webserver for the SolSafari IRGame activity

Run with start_server.sh, which will also install requirements using pip.


Remember to start your virtual encironment beforehandby running
`. venv/bin/activate`

Run it with 

`export FLASK_APP=index.py`

`flask run --host=0.0.0.0`


If process is already running use

`lsof -n -i4TCP:5000`

