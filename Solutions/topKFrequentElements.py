from collections import defaultdict
from functools import cmp_to_key
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def compareFreqTuples(t1, t2):
            if t1[0] == t2[0]:
                return 0
            elif t1[0] < t2[0]:
                return 1 # Max Heap
            else:
                return -1

        countDict = defaultdict(int)
        keyFunc = cmp_to_key(compareFreqTuples)
        for num in nums:
            countDict[num] += 1
        
        pq = []
        for num in countDict.keys():
            heapq.heappush(pq, keyFunc((countDict[num], num)))
        
        print(pq)
        res = []
        for i in range(k):
            item = heapq.heappop(pq).obj
            res.append(item[1])
        return res

from collections import defaultdict
import heapq

class SolutionHeap: # O(nlogk)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countDict = defaultdict(int)
        for num in nums: #O(n)
            countDict[num] += 1
        
        pq = [] # Min Heap of frequencies of size k
        for num in countDict.keys(): # O(nlogk)
            if len(pq) >= k: # Drop the least frequent element if heap gets too big
                leastElementInPq = heapq.heappop(pq)
                if countDict[num] > leastElementInPq[0]:
                    heapq.heappush(pq, (countDict[num], num))
                else:
                    heapq.heappush(pq, leastElementInPq)
            else:
                heapq.heappush(pq, (countDict[num], num))
        
        res = []
        for i in range(k): # O(k)
            item = heapq.heappop(pq)
            res.append(item[1])
        return res

class SolutionOptimal: # Uses QuickSelect k times
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p += 1
            nums[r],nums[p] = nums[p],nums[r]

            if p > (len(nums) - k):
                quickSelect(l, p - 1)
            elif p < (len(nums) - k):
                quickSelect(p + 1, r)
            else:
                return nums[(len(nums) - k):]

        return quickSelect(0, len(nums) - 1)

class SolutionBucketSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # O(n) maximum size since each element can occur a maximum of N times
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res