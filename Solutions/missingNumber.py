class SolutionBitManipulation:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class SolutionClever:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res += (i - nums[i])
        return res

class SolutionWithSetDifference:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        numSet = set(nums)
        allNumsFromZeroToN = set(range(0, n + 1))
        diff = list(allNumsFromZeroToN.difference(numSet))
        return diff[0]