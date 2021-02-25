# -*- coding: utf-8 -*-
"""
COE 322 Homework 02

@author: Cameron Cummins
"""

import unittest
from read_animals import addName
from generate_animals import genAnimal

class TestNames(unittest.TestCase):
    
    def test_valid_names(self):
        # Create test case
        test_animal = genAnimal()
        # Only the head and body of the generate mutant-animal is relevant to name generation
        # Test Case 1
        test_animal['head'] = "snake"
        test_animal['body'] = "bull-lion"
        self.assertEqual(addName(test_animal), "snakeous bion")
        # Test Case 2
        test_animal['head'] = "Snake"
        test_animal['body'] = "Bull-Lion"
        self.assertEqual(addName(test_animal), "snakeous bion")
        # Test Case 3
        test_animal['head'] = "sNaKe"
        test_animal['body'] = "bUlL-lIoN"
        self.assertEqual(addName(test_animal), "snakeous bion")
        # Test Case 4
        test_animal['head'] = "snake"
        test_animal['body'] = "bull"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 5
        test_animal['head'] = "snake"
        test_animal['body'] = "bull-"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 6
        test_animal['head'] = "snake"
        test_animal['body'] = "bull-313"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 7
        test_animal['head'] = "snake"
        test_animal['body'] = "123-313"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 8
        test_animal['head'] = "snake"
        test_animal['body'] = "123-bull"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 9
        test_animal['head'] = "snake"
        test_animal['body'] = "123"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 10
        test_animal['head'] = "snake"
        test_animal['body'] = "-"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 11
        test_animal['head'] = "123snake"
        test_animal['body'] = "-"
        self.assertRaises(ValueError, lambda: addName(test_animal))
        # Test Case 12
        test_animal['head'] = ""
        test_animal['body'] = ""
        self.assertRaises(ValueError, lambda: addName(test_animal))
if __name__ == '__main__':
    unittest.main()