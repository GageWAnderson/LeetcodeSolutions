#Brute force is to use backtracking and try all solutions
#Memoize that recursion and bring down the complexity
#Find all unique is making me think DP immediately

#2 pointers close in from the outside
#This does'nt get all the combos, the real solution is O(n^3)
#Need to sort the array to do the 2 pointers method! (remember this from 2sumII !)
class SolutionKSum:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums,target,k):
            res = []
            if len(nums) == 0 or nums[0]*k > target or target > nums[-1]*k:
                return res
            if k == 2:
                return twoSum(nums,target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for group in kSum(nums[i+1:], target-nums[i],k-1):
                        res.append(group + [nums[i]])
            return res
        
        def twoSum(nums,target): #Sorted input eliminates duplicates
            res = []
            lo,hi = 0, len(nums)-1
            while lo<hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]): #extra clause avoids dups
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi+1]):
                    hi -= 1
                else:
                    res.append([nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1
            return res
        
        nums.sort()
        return kSum(nums,target,4)

    # Following a similar logic, we can implement 4Sum by wrapping 3Sum in another loop. 
    # But wait - there is a catch. If an interviewer asks you to solve 4Sum, they can follow-up with 5Sum, 6Sum, 
    # and so on. What they are really expecting at this point is a kSum solution. 
    # Therefore, we will focus on a generalized implementation here.