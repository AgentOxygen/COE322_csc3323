#!/usr/bin/env python3
"""
COE 322 Midterm Project

@author: Cameron Cummins
"""

import requests
import sys

if __name__ == '__main__':
    response = requests.get(url=sys.argv[1])
    print(response.status_code)
    print(response.json())
    print(response.headers)
