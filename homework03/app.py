#!/usr/bin/env python3
"""
COE 322 Homework 03

@author: Cameron Cummins
"""

from flask import Flask
import json
app = Flask(__name__)

@app.route('/animals', methods=['GET'])
def getAnimals():
    with open("animals.json", "r") as json_file:
        userdata = json.load(json_file)
    return json.dumps(userdata, sort_keys = True, indent = 4)

@app.route('/animals/<string:body_part>/<string:var>', methods=['GET'])
def filterAnimals(body_part, var):
    ret_animals = []
    with open("animals.json", "r") as json_file:
        for animal in json.load(json_file):
            if animal[body_part] == var:
                ret_animals.append(animal)
    return str(ret_animals)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
