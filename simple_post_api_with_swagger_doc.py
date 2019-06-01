# to run this simple api:
# (1) set FLASK_APP environment variable to the name of this file
# (2) execute: python -m flask run
# see http://flask.pocoo.org/docs/1.0/cli/#application-discovery 
# for more info on FLASK_APP variable

from flask import Flask, Response, request, json, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello_username_json', methods=['POST'])
def hello_username_json():
    """Simple endpoint returning a plain old 'Hello, %USERNAME%!' string
    ---    
    parameters:
      - in: body
        name: body
        description: request body
        schema:
            type: object
            required:
              - username
            properties:
                username:
                    type: string
                    example: oserikov
    produces:
        application/json; charset=utf-8
    responses:
        '200':
            description: successful execution
            schema:
                type: object
                properties:
                    greeting:
                        type: string
                        description: the greeting string
                        example: "Hello, oserikov!"
                    just an integer:
                        type: integer
                        description: just an integer
                        example: 42
                required:
                  - greeting
            
    """
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
