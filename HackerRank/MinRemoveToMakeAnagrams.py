# Complete the makeAnagram function below.
from collections import Counter
def makeAnagram(a, b):
    if len(a) > len(b):
        a,b = b,a #a is always smaller
    a_count = Counter(a) #O(|a|)
    b_count = Counter(b) #O(|b|)
    res = 0
    for letter in "abcdefghijklmnopqrstuvwxyz": #O(26)
        res += abs(a_count[letter]-b_count[letter])
    return res