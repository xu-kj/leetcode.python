#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'suitableLocations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY center
#  2. LONG_INTEGER d
#

def suitableLocations(center, d):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    center_count = int(input().strip())

    center = []

    for _ in range(center_count):
        center_item = int(input().strip())
        center.append(center_item)

    d = int(input().strip())

    result = suitableLocations(center, d)

    fptr.write(str(result) + '\n')

    fptr.close()
