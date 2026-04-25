class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []
        seen = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        return []


# NOTE: Did this years later, need to get warmed up again
class Solution2026:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # NOTE: Return the indicies of the 2 numbers that add up to the target, not the numbers themselves

        # NOTE: Start with the brute force, then get the more optimial solution
        # TODO: Brute force is to check all possible combos in the array, with an O(n^2) time O(1) memory solution
        if len(nums) < 2:
            return []
        # for i,n1 in enumerate(nums[:(len(nums) - 1)]):
        #     starting_index_for_j = i + 1
        #     for j,n2 in enumerate(nums[starting_index_for_j:]):
        #         if n1 + n2 == target:
        #             return [i,starting_index_for_j+j]
        complements: dict[int, int] = (
            dict()
        )  # NOTE: O(n) space and O(n) time tradeoff using a hash map
        for i, n1 in enumerate(nums):
            complements[target - n1] = i
        for j, n2 in enumerate(nums):
            n2_complement_index = complements.get(n2)
            if n2_complement_index and n2_complement_index != j:
                return sorted([n2_complement_index, j])
        return []

        # TODO: Then, optimize the solution - we need to remember what numbers we've seen before to quickly check if n1+n2 adds
        # to the target without needing to loop through the whole array
        # NOTE: Can quickly look up the "complement" that adds up to the target using a hash map


s = set()
s.remove
