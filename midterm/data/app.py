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
rd = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/animals/list', methods=['GET'])
def listAnimals():
    UIDs = []
    for key in rd.keys():
        UIDs.append(key)

    return json.dumps(UIDs, indent='\t', sort_keys=True)
    
@app.route('/animals/filter/<string:body_part>/<string:var>', methods=['GET'])
def filterTypeAnimals(body_part, var):
    ret_animals = []

    for animal_uid in rd.keys():
        animal = rd.hgetall(animal_uid)
        if body_part in animal:
            if animal[body_part] == var:
                ret_animals.append(animal)
            print("Found in " + str(animal))
        else:
            print(str(body_part) + " not in dictionary: " + str(animal))
    return json.dumps(ret_animals, indent='\t', sort_keys=True)

@app.route('/animals/gen/<int:num_animals>')
def genAnimals(num_animals):
    animals = gen_animals.genAnimals(num_animals)
    
    for animal in animals:
        rd.hmset(animal["UID"], animal)

    return json.dumps(animals, indent='\t', sort_keys=True)

# query a range of dates
@app.route('/animals/date')
def filterDate():
    min_date = request.args.get('min_date')
    max_date = request.args.get('max_date')
    if min_date == "None" or min_date == None: min_date = str(datetime.MINYEAR)
    if max_date == "None" or max_date == None: max_date = str(datetime.MAXYEAR)
    
    print(min_date)
    print(max_date)

    animals = []

    for animal_uid in rd.keys():
        animal = rd.hgetall(animal_uid)
        if min_date <= animal["created_on"] <= max_date:
            animals.append(animal)
    return json.dumps(animals, indent='\t', sort_keys=True)
# delete date range
@app.route('/animals/delete/date')
def deleteDate():
    min_date = request.args.get('min_date')
    max_date = request.args.get('max_date')
    if min_date == "None" or min_date == None: min_date = str(datetime.MINYEAR)
    if max_date == "None" or max_date == None: max_date = str(datetime.MAXYEAR)

    animals = []

    for animal_uid in rd.keys():
        animal = rd.hgetall(animal_uid)
        if min_date <= animal["created_on"] <= max_date:
            rd.delete(animal_uid)
    return json.dumps(animals, indent='\t', sort_keys=True)

# selects a particular creature by its unique identifier
@app.route('/animals/uid/<string:uid>')
def filterUID(uid):
    print(uid)
    if uid in rd.keys():
        return json.dumps(rd.hgetall(uid), indent='\t', sort_keys=True)
    return "No animal with UID = " + str(uid)

# edits a particular creature by passing the UUID, and updated stats
@app.route('/animals/edit/<string:uid>')
def editByUID(uid):
    arms = str(request.args.get('arms'))
    body = str(request.args.get('body'))
    created_on = str(request.args.get('created_on'))
    head = str(request.args.get('head'))
    legs = str(request.args.get('legs'))
    tails = str(request.args.get('tails'))
    
    valid = False
    animal = None

    if uid in rd.keys():
        animal = rd.hgetall(uid)
        valid = True
    
        if not arms == "None": animal["arms"] = str(arms)
        if not body == "None": animal["body"] = str(body)
        if not created_on == "None": animal["created_on"] = str(created_on)
        if not head == "None": animal["head"] = str(head)
        if not legs == "None": animal["legs"] = str(legs)
        if not tails == "None": animal["tails"] = str(tails)
    
    if valid:
        rd.hmset(uid, animal)
        return json.dumps(animal, indent='\t', sort_keys=True)
    return "No animal with UID = " + str(uid)

# count total animals
@app.route('/animals/total')
def totalNum():
    return str(len(rd.keys()))

# returns the average number of legs per animal
@app.route('/animals/avg/legs')
def averageLegs():
    total = 0
    for uid in rd.keys():
        total += rd.hget(uid, 'arms')

    return str(total / len(rd.keys()))

@app.route('/animals/filter/<string:body_part>/<int:var>', methods=['GET'])
def filterIntAnimals(body_part, var):
    ret_animals = []
    
    for animal_uid in rd.keys():
        animal = rd.hgetall(animal_uid)
        if animal[body_part] == str(var):
            ret_animals.append(animal)
    return json.dumps(ret_animals, indent='\t', sort_keys=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
