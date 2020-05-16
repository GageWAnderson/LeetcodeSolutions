class Solution: #Too slow, O(n^3) cannot be accepted
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = set()
        seenNumbers = set()
        possibleNums = set(nums)
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1,len(nums)):
                    if(k == len(nums)): break
                    tmp = {nums[i],nums[j],nums[k]} #set of numbers currently examined
                    combo = frozenset(tmp) #Hashable, immutable unordered collection
                    #print(f"i = {i}, j= {j}, k={k}")
                    #print(f"nums[i] = {nums[i]}, nums[j] = {nums[j]}, nums[k] = {nums[k]}")
                    if(nums[i] + nums[j] + nums[k] == 0 and not combo in seenNumbers):
                        trips.add((nums[i],nums[j],nums[k]))
                        seenNumbers.add(combo) #Only track the 
                        #combonations of numbers (sets) if you have added them to the set
        return map(lambda x : list(x), trips)
        
class SolutionBetter: #Had to look this one up to gain the insight to sort the array...
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort() #Key line, essential for a simple solution
        
        length = len(nums)
        
        for i in range(length-2): #Need 2 pointers at end, range is end-exclusive, has been causing a lot of issues for me...
            if i >0 and nums[i] == nums[i-1]:
                continue #this eliminates duplicate values
            L = i+1
            R = length-1
            
            while L<R:
                total = nums[i]+nums[L]+nums[R]
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else: #total == 0
                    #The below loops deal with duplicates for L,R
                    res.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L] == nums[L+1]:
                        L += 1
                    while L<R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
        return res
                    
        #Sorting was very effective for dealing with duplicates, didn't
        #Require any kind of advanced data structures...