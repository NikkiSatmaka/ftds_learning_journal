from crypt import methods
from distutils.log import debug
from flask import Flask, request, jsonify

app = Flask(__name__)
name = "Nikki"

@app.route("/")
def hello_world():
    return f"<p>Hello {name}!</p>"

@app.route("/change", methods=["POST"])
def change_name():
    global name
    content = request.jsom
    name = content['name']
    response = jsonify(success=True, message=f'Name changed to {name}')
    return response

app.run(debug=True)