#To get the O(nlogk) solution, you need to use a heap
#Need to read the question more carefully... has to be alphabetical
from collections import Counter
from functools import cmp_to_key
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        def compare(t1,t2):
            num1,num2 = t1[1],t2[1]
            #print(f"num1 = {num1}, num2 = {num2}")
            if num1 > num2:
                return -1
            elif num1 < num2:
                return 1
            else:
                s1,s2 = t1[0],t2[0]
                i = 0
                while i < len(s1) and i < len(s2):
                    #print(f"c1 = {s1[i]}, c2 = {s2[i]}")
                    if s1[i] < s2[i]:
                        return -1
                    elif s1[i] > s2[i]:
                        return 1
                    else:
                        i += 1
                if len(s1) < len(s2): #Want shorter words to come first, need custom cmp for this
                    return -1
                elif len(s1) > len(s2):
                    return 1
                else:
                    return 0
        
        counter = Counter(words) #O(nk)
        most_freq = counter.most_common()
        canidates = []
        nums_considered = set()
        i = 0
        while i < len(most_freq) and len(nums_considered) <= k:
            canidates.append(most_freq[i])
            nums_considered.add(most_freq[i][1])
            i += 1
        canidates.sort(key = cmp_to_key(compare)) 
        return [canidates[x][0] for x in range(k)]

#This one was annoying due to the required custom compare function

import heapq
from collections import Counter
#Need to limit the size of the heap to k to keep complexity as O(nlogk) rather than O(nlogn)
class SolutionHeap:
    def topKFrequent(self, words, k):
        counter = Counter(words) #O(n)
        items = [(-item[1],item[0]) for item in counter.items()] #O(n)
        word_heap = heapq.heapify(items)
        return [heapq.heappop(items)[1] for _ in range(k)]
            