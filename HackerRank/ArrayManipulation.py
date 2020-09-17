#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
# O(n) time, O(n) space
def arrayManipulation(n, queries):
    max_len = max(queries,key = lambda x: x[1])[1] + 1 #O(n)
    arr = [0 for x in range(max_len)] #Inclusive, so ends at max_len
    for q in queries:
        a,b,k = q
        arr[a-1] += k
        arr[b] -= k
        
    max_acc_slope = arr[0] #Don't know to start @ 0
    acc_slope = arr[0]
    for i in range(1,max_len):
        acc_slope += arr[i]
        max_acc_slope = max(acc_slope,max_acc_slope)

    return max_acc_slope

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

# After contemplating the popular approach for solving this, here is how I wrapped my head around it.

# For every input line of a-b-k, you are given the range (a to b) where the values increase by k. So instead of keeping track of actual values increasing, just keep track of the rate of change (i.e. a slope) in terms of where the rate started its increase and where it stopped its increase. This is done by adding k to the "a" position of your array and adding -k to the "b+1" position of your array for every input line a-b-k, and that's it. "b+1" is used because the increase still applied at "b".

# The maximum final value is equivalent to the maximum accumulated "slope" starting from the first position, because it is the spot which incremented more than all other places. Accumulated "slope" means to you add slope changes in position 0 to position 1, then add that to position 2, and so forth, looking for the point where it was the greatest.