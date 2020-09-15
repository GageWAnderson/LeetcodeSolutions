#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
from collections import Counter
def repeatedString(s, n):
    if len(s) == 0: return 0
    count = Counter(s)
    stop = n % len(s)
    chopped_off = s[:stop]
    chop_counter = Counter(chopped_off)
    return (n//len(s))*count["a"] + chop_counter["a"]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()