#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
# Brute force is to get all substrings for each
# And see if there is any overlap
# O(n^2) to generate all substs. for 1 word
# Don't need to check longer substrings, just need
# To make sure they have same chars
def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

#The clever solution for this problem was super easy
#Just need to have your brain on a bit!