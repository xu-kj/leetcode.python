#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumFruits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY fruits as parameter.
#

def getMinimumFruits(fruits):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fruits_count = int(input().strip())

    fruits = []

    for _ in range(fruits_count):
        fruits_item = int(input().strip())
        fruits.append(fruits_item)

    result = getMinimumFruits(fruits)

    fptr.write(str(result) + '\n')

    fptr.close()
