from flask import Flask, jsonify
from python_module.python_module import hello_world

app = Flask(__name__)

@app.route("/")
def api_hello_world():
    return jsonify(hello_world())
