#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    update = (d % len(a))
    print(f"update = {update}")
    new_array = [0 for x in range(len(a))]
    if update == 0: return a
    for i in range(len(a)):
        new_index = (i - update) % len(a)
        print(new_index)
        new_array[new_index] = a[i]
    return new_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
