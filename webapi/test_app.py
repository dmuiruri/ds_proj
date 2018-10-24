from flask import Flask, request
import json


'''

 This is just for experimenting.
 Rename to app.py (Flask default server file name) to run.

'''

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello():
    return json.dumps({'message': 'Hello space!'})


@app.route("/predict", methods=['POST'])
def predict():
    f = request.files['files']
    return json.dumps({'message': 'This is a consumption forecast.'})

