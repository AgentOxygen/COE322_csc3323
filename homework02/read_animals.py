#usr/bin/env python3
"""
COE 322 Homework 01

@author: Cameron Cummins
"""

import json
import random as rand
import sys

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

# This is the new feature :)
def addName(animal:dict) -> str:
    """
    Parameters
    ----------
    animal : dict
        standard dictionary containing animal characteristics

    Returns
    -------
    str
        name generated based on characteristics
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
    return (first_word + " " + second_word).lower()

if __name__ == "__main__":
    getAnimals(sys.argv)