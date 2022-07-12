class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total >> 2
        nums = []
        for n in matchsticks:
            if n > target:
                return False
            elif n < target:
                nums.append(n)

        if nums == []:
            return True
        k = 4 - (len(matchsticks) - len(nums))
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def helper(nums, used, start, target, sum, k):
            if k == 1:
                return True

            i = start
            while i < len(nums):
                if not used[i]:
                    used[i] = True
                    if sum + nums[i] < target and helper(nums, used, i + 1, target, sum + nums[i], k):
                        return True
                    if sum + nums[i] == target and helper(nums, used, 0, target, 0, k - 1):
                        return True
                    used[i] = False
                    while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                        i += 1
                    if sum == 0:
                        return False
                i += 1
            return False

        return helper(nums, used, 0, target, 0, k)