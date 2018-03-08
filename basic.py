import math
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    my_name = {
        "name": "Ethan"
    }
    return jsonify(my_name)

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    my_message = {
        "message": "Hello there, {0}".format(name)
    }
    return jsonify(my_message)

@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()
    x1 = r["a"][0]
    y1 = r["a"][1]
    x2 = r["b"][0]
    y2 = r["b"][1]
    d = math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))
    my_distance = {
        "distance": d,
        "a": r["a"],
        "b": r["b"]
    }
    return jsonify(my_distance)
