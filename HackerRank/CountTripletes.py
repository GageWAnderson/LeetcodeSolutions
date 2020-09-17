# Complete the countTriplets function below.
# Triplets must be increasing indicies, but can be non-contiguous
# Duplicates are allowed
from collections import defaultdict
class SolutionSlow:
    def countTriplets(arr, r):
        index_set = defaultdict(set)
        res = 0
        for i in range(len(arr)):
            #print(index_set)
            n1 = arr[i]//r
            n2 = n1//r
            print(f"n1 = {n1}, n2 = {n2}")
            if n1 in index_set and n2 in index_set:
                #print(index_set)
                i1s = index_set[n1]
                i2s = index_set[n2]
                #Increase answer by the number of pairs here
                for i1 in i1s:
                    for i2 in i2s:
                        if i1 > i2:
                            res += 1
            index_set[arr[i]].add(i)
        return res

# My first solution was too inefficent, kept timing out
# No idea why, it is similar to other hash-map solutions
# Best solution maintains an occurence map of elems on
# Left, right sides of the current elem
from collections import defaultdict
class SolutionFast:
    def countTriplets(arr, r):
        if len(arr) <=2: return 0
        left_map = defaultdict(int)
        right_map = defaultdict(int)
        for i in range(len(arr)):
            right_map[arr[i]] += 1
        res = 0
        for i in range(len(arr)):
            right_map[arr[i]] -= 1 #Remove from right map
            left = arr[i]//r
            right = arr[i]*r
            if (arr[i]%r == 0) and left in left_map and right in right_map:
                res += left_map[left]*right_map[right]
            left_map[arr[i]] += 1
        return res

#Forgot to check (arr[i]%r == 0) stupid mistake!