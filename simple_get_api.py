# to run this simple api:
# (1) set FLASK_APP environment variable to the name of this file
# (2) execute: python -m flask run
# see http://flask.pocoo.org/docs/1.0/cli/#application-discovery 
# for more info on FLASK_APP variable

from flask import Flask, Response

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    # возвращает html-страницу
    return 'Hello, World!'

@app.route('/hello_world_string')
def hello_world_string():
    # возвращает просто строку
    response_string = "Hello, World!"
    content_type = "text/plain; charset=utf-8"

    response = Response(response=response_string, content_type=content_type, status=200)
    return response
