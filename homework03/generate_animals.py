#!/usr/bin/env python3
"""
COE 322 Homework 01 Updated for Homework 02

@author: Cameron Cummins
"""

import json
import petname as pn
import random as rand
import sys

def getRandMultiple(min_rand:int, max_rand:int, fact_rand:int) -> int:
    """
    Parameters
    ----------
    min_rand : int
        minimum integer in range of random numbers (inclusive)
    max_rand : int
        maximum integer in range of random numbers (inclusive)
    fact_rand : int
        required factor for random number selected (it will be a multiple of this integer)

    Returns
    -------
    int
        random integer that is a multiple of the specified factor and within the specified range
        raises an IndexError if no valid integer is possible
    """
    
    # Calculate all multiples within the range
    possible_nums = []
    num = min_rand
    while num <= max_rand:
        if num % fact_rand == 0:
            possible_nums.append(num)
            num += fact_rand
        else:
            num += 1
    return rand.choice(possible_nums)
    
def genAnimal() -> dict:
    """
    Returns
    -------
    dict
        A complete description of a generated animal according to Dr. Moreau's specifications:
            - A head randomly chosen from this list: snake, bull, lion, raven, bunny
            - A body made up of two animals randomly chosen using the petname library
            - A random number of arms; must be an even number and between 2-10, inclusive
            - A random number of legs; must be a multiple of three and between 3-12, inclusive
            - A non-random number of tails that is equal to the sum of arms and legs
    """
    animal = {}
    heads = ["snake", "bull", "lion", "raven", "bunny"]
    animal["head"] = heads[rand.randint(0, len(heads) - 1)]
    animal["body"] = pn.generate(words = 1) + "-" + pn.generate(words = 1)
    animal["arms"] = getRandMultiple(2, 10, 2)
    animal["legs"] = getRandMultiple(3, 12, 3)
    animal["tails"] = animal["arms"] + animal["legs"]
    return animal

def genAnimals(num_of_animals:int) -> list:
    """
    Parameters
    ----------
    num_of_animals : int
        number of mutant animals to generate

    Returns
    -------
    list
        list of of generated mutant animals
    """
    animals = []
    for num in range(num_of_animals):
        animals.append(genAnimal())
    return animals
    
def genAnimalsJSON(num_of_animals:int, path:str) -> None:
    """
    Parameters
    ----------
    num_of_animals : int
        number of mutant animals to generate
    path : str
        location to output JSON file to

    Returns
    -------
    None
        outputs list of dictionaries containing information on randomly generated mutant animals to specified JSON file location
    """
    animals = genAnimals(num_of_animals)
    with open(path, 'w') as output:
        json.dump(animals, output, indent=2)
                
if __name__ == "__main__":
    genAnimalsJSON(20, sys.argv[1])
