# -*- coding: utf-8 -*-
"""
COE 322 Homework 01

@author: Cameron Cummins
"""

import json
import random as rand


def getAnimals(path:str) -> list:
    """
        Gets animals from .json file and returns them in a list
        'path' is a string that specifies the path to the .json file containing information on the animals
    """
    with open(path, 'r') as input_file:
        animals = json.load(input_file)
    return animals

def printRandomInfo(path:str) -> None:
    """
        Prints information on a random animal specifed in a .json fie
        'path' is a string that specifies the path to the .json file containing information on the animals
    """
    animals = getAnimals(path)
    animal = animals[rand.randint(0, len(animals) - 1)]
    print("Head: " + animal["head"])
    print("Body: " + animal["body"])
    print("Arms: " + str(animal["arms"]))
    print("Legs: " + str(animal["legs"]))
    print("Tails: " + str(animal["tails"]))
    
if __name__ == "__main__":
    printRandomInfo("animals.json")