# Brute force is to try all the contiguous subarrays O(n^2)
# Very close to right on the first try
# Missed 2 edge cases: All numbers are 0 and First number = k
from collections import Counter


class Solution:  # O(n) time and space, uses a hash set to track sums seen so far
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] if nums[0] == k else 0
        res = 0
        seen_so_far = Counter()  # Sums already seen, counts duplicates
        prev_sum = 0
        for i in range(len(nums)):
            # print(seen_so_far)
            curr_sum = prev_sum + nums[i]
            diff = curr_sum - k
            if diff == 0:
                res += 1
            if diff in seen_so_far:
                res += seen_so_far[diff]
            seen_so_far[curr_sum] += 1
            prev_sum = curr_sum

        return res


# 2 pointers, move up the left pointer when you go over k and increment res by 1
# That solution only works when we don't have any negative values allowed
# Hash map solution for seen sums works for arrays with all values

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
                res += seen_sums[cum_sum - k]
            seen_sums[cum_sum] += 1

        return res


# This is the exact type of problem that you should jump to hashmap usage
#
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TODO: Get the brute force, then optimize it
        # if len(nums) < 1:
        #     return 0
        # ans = 0

        # for i,n1 in enumerate(nums):
        #     curr_array_sum = 0
        #     for j,n2 in enumerate(nums[i:]):
        #         curr_array_sum += n2
        #         if curr_array_sum == k:
        #             ans += 1
        # return ans

        # NOTE: Problems that have negative values with cumulative sums disrupt you from being able to use the sliding window
        # Disregard sliding window suggestion, I see now the problem states negative values are possible (which discounts the use of sliding window)
        seen_sums = defaultdict(int)
        seen_sums[0] = 1
        cum_sum = 0
        res = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if seen_sums[cum_sum - k] > 0:
                res += seen_sums[cum_sum - k]
            seen_sums[cum_sum] += 1

        return res

        # Incorrect solution, over-indexed on sliding window approach when that wasn't the correct approach to the problem
        # Data structure with prefix sums + frequency maps of sums was correct though
        # NOTE: Prefix/postfix sums - How much does the array sum to at any given point
        # NOTE: Subtract all elements we've seen so far, except for the sum currently in the window
        # Check if the complement of that number to get k is in the prefix sums on the right of j
        # If yes, then advance j
        # If no, then advance i until the complement of the current sum is on the right of j
        # if len(nums) < 1:
        #     return 0

        # ans = 0
        # i, j = 0, 0
        # curr_window_sum = 0
        # prefix_sums_by_position = self.get_prefix_sums_by_position(nums)
        # prefix_sum_freq_map = self.build_prefix_sums_freq_map(prefix_sums_by_position)

        # while i < j and j < len(nums):
        #     curr_window_sum += nums[j]

        #     curr_window_complement_in_prefix_sum_freq_map = 0
        #     if i > 0:
        #         curr_window_complement_in_prefix_sum_freq_map = k - curr_window_sum - prefix_sums_by_position[i-1]
        #     else :
        #         curr_window_complement_in_prefix_sum_freq_map = k - curr_window_sum

        #     while curr_window_complement_in_prefix_sum_freq_map in prefix_sum_freq_map:

        #     if curr_window_sum == k:
        #         ans += 1

        # def build_prefix_sums_freq_map(self, prefix_sums_by_position: Dict[int, int]) -> Dict[int, int]:
        #     freq_map = defaultdict(int)
        #     for prefix_sum in prefix_sums_by_position:
        #         freq_map[prefix_sum] += 1
        #     return freq_map

        # def get_prefix_sums_by_position(self, nums: List[int]) -> Dict[int, int]:
        #     ans = dict()
        #     curr_sum = 0
        #     for i,n in enumerate(nums):
        #         curr_sum += n
        #         ans[i] = n
        # return ans
