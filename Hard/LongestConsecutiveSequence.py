#Build some set of groups of elements that are next to each other,
#Then pass through those sets and join them
#Requires O(n) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: #This solution is space-inefficient, only need to allocate 1 set
        if len(nums) == 0: return 0
        runs = []
        numSet = set(nums) #O(1) lookup time for edges of expanding window
        for item in nums: #O(n)
            run = [item]
            lower,upper = item,item
            while numSet:
                #print(numSet)
                if upper+1 in numSet:
                    run.append(upper+1)
                    numSet.remove(upper+1)
                    upper += 1
                elif lower-1 in numSet:
                    run.append(lower-1)
                    numSet.remove(lower-1) #Remove returns None
                    lower -= 1
                else:
                    break
            runs.append(run)
        return len(max(runs,key = lambda x : len(x))) #Forgot len here