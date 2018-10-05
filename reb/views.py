 
import os, inspect
import json
from flask import render_template, jsonify
from reb import app
from pprint import pprint


# get project root dir
CURR_DIR = os.path.dirname(inspect.getabsfile(inspect.currentframe()))
ROOT_DIR = os.path.dirname(CURR_DIR)


# home route
@app.route("/home")
@app.route("/index.html")
@app.route("/index")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict/PAYEMS/<variables>/<target>")
def predict_payemns(variables, target):
    print(variables)
    print(target)

    d = {"a": [1, 2, 3], "b": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/W875RX1/<variables>/<target>")
def predict_w875rx1(variables, target):
    print(variables)
    print(target)

    d = {"d": [1, 2, 3], "e": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/INDPRO/<variables>/<target>")
def predict_indpro(variables, target):
    print(variables)
    print(target)

    d = {"f": [1, 2, 3], "g": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/CMRMTSPL/<variables>/<target>")
def predict_cmrmtspl(variables, target):
    print(variables)
    print(target)

    d = {"h": [1, 2, 3], "j": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/<variables>/<target>")
def predict(variables, target):
    print(variables)
    print(target)
    ffname = os.path.join(ROOT_DIR, "reb", "data", "int", "sample_data.json")
    with open(ffname) as fp:
        data = json.load(fp)

    d = {"z": [1, 2, 3], "r": [4, 5, 6]}
    return jsonify(data)



