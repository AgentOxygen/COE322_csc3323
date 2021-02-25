# -*- coding: utf-8 -*-
"""
COE 322 Homework 01 Updated for Homework 02

@author: Cameron Cummins
"""

import json
import petname as pn
import random as rand

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
    for animal in animals:
        addName(animal)
    with open(path, 'w') as output:
        json.dump(animals, output, indent=2)

# This is the new feature :)
def addName(animal:dict) -> dict:
    """
    Parameters
    ----------
    animal : dict
        animal dictionaries

    Returns
    -------
    dict
        same dictionary that describes an animal but with a name added to it
        the manner in which names are generated and added are as follows:
            - The first word in the name is the head followed by the suffix "ous"
            - The second word in the name is the first letter of the first word of the body, followed by
                the second word of the body parsed to the first vowel
    """
    
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    # Check that first word is alphabetic
    if animal['head'].isalpha():
        first_word = animal["head"] + "ous"
    else:
        raise ValueError('"head" attribute must be alphabetic')
    second_word = ""
    # Build second word by parsing body description
    first_body, second_body = animal["body"].split("-")
    # Check to make sure body words are alphabetic
    if not first_body.isalpha() or not second_body.isalpha():
        raise ValueError('"body" attribute must have only alphabetic words')
    # Check to make sure second body word is valid (has vowel and consonance)
    has_vowel, has_other_letter = False, False
    for char in second_body.upper():
        if char in vowels:
            has_vowel = True
        elif char.isalpha():
            has_other_letter = True
    if not (has_vowel and has_other_letter):
        raise ValueError('"body" attribute must have a valid two-word, alphabetic combination with the second word containing at least one vowel and one other letter')
    # Parse second word in body to include everything past the vowel
    for index, char in enumerate(second_body.upper()):
        if char in vowels:
            second_word = first_body[0] + second_body[index::]
            break
    # Add name
    animal['name'] = (first_word + " " + second_word).lower()
    return animal
                
if __name__ == "__main__":
    genAnimalsJSON(20, "animals.json")