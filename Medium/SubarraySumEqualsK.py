#Brute force is to try all the contiguous subarrays O(n^2)
#Very close to right on the first try
#Missed 2 edge cases: All numbers are 0 and First number = k
from collections import Counter
class Solution: #O(n) time and space, uses a hash set to track sums seen so far
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return nums[0] if nums[0] == k else 0
        res = 0
        seen_so_far = Counter() #Sums already seen, counts duplicates
        prev_sum = 0
        for i in range(len(nums)):
            #print(seen_so_far)
            curr_sum = prev_sum + nums[i]
            diff = curr_sum - k
            if diff == 0:
                res += 1
            if diff in seen_so_far:
                res += seen_so_far[diff]
            seen_so_far[curr_sum] += 1
            prev_sum = curr_sum
        
        return res

#2 pointers, move up the left pointer when you go over k and increment res by 1
#That solution only works when we don't have any negative values allowed
#Hash map solution for seen sums works for arrays with all values

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen_sums = defaultdict(int)
        seen_sums[0] = 1
        cum_sum = 0
        res = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if seen_sums[cum_sum - k] > 0:
                res += seen_sums[cum_sum-k]
            seen_sums[cum_sum] += 1
            
        return res


#This is the exact type of problem that you should jump to hashmap usage