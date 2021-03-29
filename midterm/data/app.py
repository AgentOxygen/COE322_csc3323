#!/usr/bin/env python3
"""
COE 322 Midterm Project

@author: Cameron Cummins
"""

from flask import Flask, request
import generate_animals as gen_animals
import read_animals
import json, datetime, redis

app = Flask(__name__)
rd = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/animals', methods=['GET'])
def loadAnimals():
    list_name = request.args.get('list')
    if list_name == None:
        return json.dumps(read_animals.getAnimals("animals.json"), indent='\t', sort_keys=True)
    return json.dumps(read_animals.getAnimals(list_name + ".json"), indent='\t', sort_keys=True)
    
@app.route('/animals/<string:body_part>/<string:var>', methods=['GET'])
def filterTypeAnimals(body_part, var):
    ret_animals = []
    
    list_name = request.args.get('list')
    if list_name == None: list_name = "animals"
    
    for animal in read_animals.getAnimals(list_name + ".json"):
        if animal[body_part] == var:
            ret_animals.append(animal)
    return json.dumps(ret_animals, indent='\t', sort_keys=True)

@app.route('/animals/gen/<int:num_animals>')
def genAnimals(num_animals):
    list_name = request.args.get('list')
    if list_name == None: list_name = "animals"
    
    gen_animals.genAnimalsJSON(num_animals, "./" + list_name + ".json")
    return "Generated '" + list_name + ".json' with " + str(num_animals) + " animals"

# query a range of dates
@app.route('/animals/date')
def filterDate():
    list_name = request.args.get('list')
    min_date = request.args.get('min_date')
    max_date = request.args.get('max_date')
    if list_name == None: list_name = "animals"
    if min_date == None: min_date = str(datetime.MINYEAR)
    if max_date == None: max_date = str(datetime.MINYEAR)
    
    return str(min_date) + " - " + str(max_date)
    


# selects a particular creature by its unique identifier

# edits a particular creature by passing the UUID, and updated stats

# deletes a selection of animals by a date ranges

# returns the average number of legs per animal

# returns a total count of animals

@app.route('/animals/<string:body_part>/<int:var>', methods=['GET'])
def filterIntAnimals(body_part, var):
    ret_animals = []
    
    list_name = request.args.get('list')
    if list_name == None: list_name = "animals"
    
    for animal in read_animals.getAnimals(list_name + ".json"):
        if animal[body_part] == var:
            ret_animals.append(animal)
    return json.dumps(ret_animals, indent='\t', sort_keys=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
