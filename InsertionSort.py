#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    last_element = arr[-1]
    
    for i in range(n-1,-1,-1):
        if arr[i-1] > last_element and i != 0:
            arr[i] = arr[i-1]
            print(*arr)
        else:
            arr[i] = last_element
            print(*arr)
            break 
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
