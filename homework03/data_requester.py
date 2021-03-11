#!/usr/bin/env python3
"""
COE 322 Homework 03

@author: Cameron Cummins
"""

import requests
import sys

if __name__ == '__main__':
    response = requests.get(url=sys.argv)
    print(response.status_code)
    print(response.json())
    print(response.headers)
