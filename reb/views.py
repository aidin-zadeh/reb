 
import os, inspect
from flask import render_template, jsonify
from reb import app


# get project root dir
CURR_DIR = os.path.dirname(inspect.getabsfile(inspect.currentframe()))
ROOT_DIR = os.path.dirname(CURR_DIR)


# home route
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


# @app.route("predict/<variables>/<target>")
# def predict(variables, target):
#     print(variables)
#     print(target)
#     render_template("index.html")


