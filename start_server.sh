. venv/bin/activate
pip install -r requirements.txt

#Kill all the stuff that uses port 5000 (I have not idea if this runs on luinux or windows)
lsof -P | grep ':5000' | awk '{print $2}' | xargs kill -9

export FLASK_APP=index.py

flask run --host=0.0.0.0

