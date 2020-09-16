#!/bin/python3

import math
import os
import random
import re
import sys

#Well, I know that if a number is already in its place, don't swap it
#Just do selection sort and count the number of swaps? (Brute-Force)
#KEY TIME SAVER: use an index_dict to do const. time index lookup
#Note: assumes consecutive values
def minimumSwaps(arr): #Selection sort will make the min swap number
    #Some way to truncate selection sort?
    #Maybe use a hash dict to track the remaining unsorted elements
    #If you swap elements into the correct positions, 
    num_swaps = 0
    index_dict = {arr[i]:i for i in range(len(arr))}
    for i in range(len(arr)):
        if arr[i] == i + 1:
            continue
        index = index_dict[i + 1] #Assumes consecutive
        index_dict[arr[i]] = index
        arr[i],arr[index] = arr[index],arr[i]
        del index_dict[i + 1]
        num_swaps += 1
    
    return num_swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()