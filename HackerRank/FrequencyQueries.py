#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
from collections import Counter
def freqQuery(queries):
    res = []
    freq_dict = Counter()
    freqs_in_dict = Counter()
    for L in queries:
        op,elem = L[0],L[1]
        if op == 1:
            curr_freq = freq_dict[elem]
            if curr_freq != 0:
                freqs_in_dict[curr_freq] -= 1
            freqs_in_dict[curr_freq+1] += 1
            freq_dict[elem] += 1
        elif op == 2:
            curr_freq = freq_dict[elem]
            if curr_freq != 0:
                freqs_in_dict[curr_freq] -= 1
                freqs_in_dict[curr_freq-1] += 1
                freq_dict[elem] -= 1
        elif op == 3:
            if freqs_in_dict[elem] > 0: #O(1)
                res.append(1)
            else:
                res.append(0)
    return res
        #Return List[int] where elem=1 if
        #There is >= 1 elem in curr_array, 0 if not
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
