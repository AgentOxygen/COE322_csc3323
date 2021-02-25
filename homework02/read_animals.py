# -*- coding: utf-8 -*-
"""
COE 322 Homework 01

@author: Cameron Cummins
"""

import json
import random as rand


def getAnimals(path:str) -> list:
    """
    Parameters
    ----------
    path : str
        location of JSON file to read

    Returns
    -------
    list
        list of dictionaries containing information on the animals from the JSON file
    """
    with open(path, 'r') as input_file:
        animals = json.load(input_file)
    return animals

def printRandomInfo(path:str) -> None:
    """
    Parameters
    ----------
    path : str
        location of JSON file to read

    Returns
    -------
    None
        reads specified JSON file, randomly selects an animal from it, and prints the information on that animal to the console
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