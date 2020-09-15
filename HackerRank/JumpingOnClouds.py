#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c) <= 3: return 1
    dp =[0 for x in range(len(c))]
    dp[1] = 1 if c[1] == 0 else float("inf")
    dp[2] = 1 if c[2] == 0 else float("inf")

    for i in range(3,len(c)):
        if c[i] == 1: #Forgot to account for invalid
            dp[i] = float("inf")
        else:
            dp[i] = min(dp[i-1],dp[i-2]) + 1
    print(dp)
    return dp[len(c)-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()