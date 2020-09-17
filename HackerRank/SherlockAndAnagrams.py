#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
# Brute force is O(n^2), find all the disjoint substrings, hash their
# Letters, and see which entries are greater than 1
from collections import defaultdict
def sherlockAndAnagrams(s):
    seen = defaultdict(int)
    def nC2(num): #n elements, choose 2 (combonations)
        return math.factorial(num) // (2*math.factorial(num-2))
        #Not working because frozenset is not a multiset
    
    def get_letter_count_tuple(sub):
        res = [0]*26
        for c in sub:
            res[ord(c)%26] += 1
        return tuple(res)

    for sub_len in range(1,len(s)):
        j = 0
        #Anagrams must be the same length
        while j + sub_len < len(s)+1:
            #print(f"j = {j}")
            #print(f"j+sub_len = {j+sub_len}")
            subst = s[j:j+sub_len]
            seen[get_letter_count_tuple(subst)] += 1
            j += 1
    res = 0
    print(seen)
    for v in list(seen.values()):
        if v >= 2:
            res += nC2(v)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#This one was about
#1. Getting distinct substrings (easy)
#2. Hashing anagrams as a len = 26 tuple (easy)
# Recognizing that I needed an O(n^3) solution since you need to look at all substs.