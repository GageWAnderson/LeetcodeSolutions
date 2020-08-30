#Brute force would be to find all the permutations and then find the one that is 
#Greater than the current nums in value O(n!) to find permutations

#The O(n) solution is very non-trivial
#However, the O(nlogn) solution using sorted is more common
#I need to be willing to examine O(nlogn) solutions if I can't possibly think of an O(n) answer
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        pointer = length - 2
        
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
        
        if pointer == -1:
            return nums.reverse()
        
        for x in range(length - 1, pointer, -1):
            if nums[pointer] < nums[x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]
                break
        
        nums[pointer + 1:] = reversed(nums[pointer + 1:])


# Comments were universally opposed to this as way too hard for a medium question.
# Needed to clarify if all numbers in a given contiguous range are present. This may have helped me find the location where I needed to swap. However, I would not have gotten the reverse the last part of the array without help.
# I had no idea what was going on once my original solution failed…
# Very difficult problem and entirely unreasonable to ask in an interview without heavy hints, but not completely impossible to solve on your own. First of all, the requirements of in-place replacement and constant space should immediately indicate swapping (this goes for other questions too). Secondly, it should be obvious that if the elements are increasing from the right, they are currently at their largest possible permutation, so nothing can be done. I think the tricky part is simply knowing where to swap and reversing the last digits. This problem is certainly at the harder-end of medium, or even hard itself.
