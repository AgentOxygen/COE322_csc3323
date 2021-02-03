# -*- coding: utf-8 -*-
"""
COE 322 Homework 01

@author: Cameron Cummins
"""

import json
import petname as pn
import random as rand

def genAnimal() -> dict:
    """
        Generates and returns a dictionary to describe a mutant animal.
    """
    animal = {}
    heads = ["snake", "bull", "lion", "raven", "bunny"]
    animal["head"] = heads[rand.randint(0, len(heads) - 1)]
    animal["body"] = pn.generate(words = 1) + "-" + pn.generate(words = 1)
    animal["arms"] = rand.randint(2, 10)
    animal["legs"] = rand.randint(3, 12)
    animal["tails"] = animal["arms"] + animal["legs"]
    return animal

def genAnimals(num_of_animals:int) -> list:
    """
        Generates and returns a list of mutant animals
        'num_of_animals' is an integer that specifies the number of animals to generate
    """
    animals = []
    for num in range(num_of_animals):
        animals.append(genAnimal())
    return animals
    
def genAnimalsJSON(num_of_animals:int, path:str) -> None:
    """
        Generates and exports a list of mutant animals
        'num_of_animals' is an integer that specifies the number of animals to generate
        'path' is a string that specifies path to create or overwrite a .json file
    """
    animals = genAnimals(num_of_animals)
    with open(path, 'w') as output:
        json.dump(animals, output, indent=2)
        
if __name__ == "__main__":
    genAnimalsJSON(20, "animals.json")