#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
#Possible for a given config to be impossible

#Impossible if A[i] > i + 2
#Minimum value to get to a given state suggests a DP solution
#What are the sub-problems?
#Init DP to zero
#dp[i] = dp[i-1] if q[i] = i+1
#dp[i] = dp[i-1] + 1 if q[i] = i+2

#Note, DP is not directly necessary here since we only know the
#Number of bribes simply by looking at a person
def minimumBribes(q):
    if len(q) <= 1: return 0
    num_bribes = 0

    for i in range(len(q)):
        #print(q[i])
        add = q[i] - i - 1
        #print(f"add = {add}")
        if add > 2:
            print("Too chaotic")
            return

        #Now, need to count the number of people that overtake
        #A given person in line
        for j in range(max(0,q[i]-2),i):
            if q[j] > q[i]:
                num_bribes += 1
    print(num_bribes)
#I over-complicated this question with DP

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

#I totally underestimated this question, thought it was DP
#But, it really was a simple logic/arrays question