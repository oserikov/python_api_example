# to run this simple api:
# (1) set FLASK_APP environment variable to the name of this file
# (2) execute: python -m flask run
# see http://flask.pocoo.org/docs/1.0/cli/#application-discovery 
# for more info on FLASK_APP variable

from flask import Flask, Response, request, json, jsonify

app = Flask(__name__)

@app.route('/hello_username_string', methods=['POST'])
def hello_username_string():
    body = request.get_json()
    username = body["username"]
    
    response_string = f"Hello, {username}!"
    content_type = "text/plain; charset=utf-8"

    response = Response(response=response_string, content_type=content_type, status=200)
    return response


@app.route('/hello_username_json', methods=['POST'])
def hello_username_json():
    body = request.get_json()
    username = body["username"]
    
    response_string = f"Hello, {username}!"
    response_dict = {
        "greeting" : response_string,
        "just an integer" : 42
    }
    response_json = json.dumps(response_dict)
    content_type = "application/json; charset=utf-8"

    response = Response(response=response_json, content_type=content_type, status=200)
    return response
