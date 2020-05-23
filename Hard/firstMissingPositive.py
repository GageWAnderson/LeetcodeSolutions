#Brute force: Sort the array, then loop through it
#Compare 2 elements, if the difference between them is greater than 1, the smallest pos
#Missing integer is 1 greater than the lower of the 2 numbers you're comparing, return
#Else continue (overall nlog(n))

#Better solution most likely does this in 1 pass...
#Loop through the array and make a min-heap out of the data (O(N))
#Then remove elements from the min-heap until you find an element whose difference with the last
#Element is greater than 1, then the answer is the last element looked at plus 1 (start at 1)
#If you get to the end, return the maximum + 1 (This is overall O(N))
#Overall is O(NlogN)

#Also, I need to clarify the input... (negative numbers are allowed)
import heapq
class Solution: #(O(Nlog(N)), still a little better than the brute force)
    def firstMissingPositive(self, nums: List[int]) -> int:
        if(len(nums) == 0): return 1 #Default answer
        heapq.heapify(nums) #O(N)
        start,res,smallest = 0,1,0 #First Positive integer
        while nums: #Do this until the heap is empty (O(Nlog(N)))
            smallest = heapq.heappop(nums) #O(log(N))
            if(smallest <= 0): continue #Handle negatives
            elif(smallest - start > 1):
                res = start + 1
                break
            start = smallest #Remember to update start!
        if(res == 1 and start > 0): return smallest + 1
        return res


#Now for the (harder) O(N), in-place O(1) space way of doing it...

#Had to look at the solutions, this is a really complex one I found:
# 0. This solution modifies the source array. But since there is no constraint for us not to do that, that's ok.
# 1. The idea is to mark array indexes that correspond to positive numbers in the array.
# 2. We'll mark the index by storing a negative value there.
# 3. But what if there's already negative value there?
# 4. To remedy this we'll first find whatever positive number there exists in array
#         and substitute all negatives and zeroes with that value.
#         This way we will not introduce a NEW positive number.
#         Obviously, if there is no positive number found at this step, the result will be 1.
# 5. After getting rid of negatives and zeroes we'll run thru array and for every number in the array
#         we will make the number at the corresponding index (number-1) negative.
#         Should check that this index is valid for the array.
# 6. If we hit a position where the number is already negative, that would mean there was a number before
#        that corresponds to that position. But we know that me made all numbers in the array to be positive.
#        So we just ignore the minus sign and execute step 5 on this position as though the number was positive.
# 7. In the end we'll have one of two cases:
# 7a. All numbers in the array are negative.
#         That means that we have numbers in the array corresponding to all indexes.
#         Obviously that means that we have ALL the numbers from 1 to nums.length (both inclusive).
#         Obviously we can have more numbers in this case, so the result is nums.length+1
# 7b. Some numbers are negative, some are positive in the array.
#         The first index with the positive number is our result - because there no such number that would
#         correspond to this index.
# 8. Mind the fact that array indexes are zero based
# 9. If there were a explicitly stated constraint that nums.length<Integer.MAX_VALUE
#         (or whatever equivalent is there for this in your preferred language)
#         we could have simply changed all negatives and zeroes to nums.length+1.
#         This way they couldn't have meddle at step 5.

#One key piece of information you can use to figure this stuff out is that we are looking for POSITIVE numbers- this allows
#Us to use negatives to mark positions in the array
class SolutionTryingTooHard: #O(N) time, O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        firstPos = len(nums) + 1
        posFound = False
        
        for i in range(len(nums)):
            if nums[i] <= 0: nums[i] = firstPos #Replace all the negatives and zeros (it seems like this isn't destructive...)
            else: posFound = True
        if not posFound: return 1
        
        #If we hit an index where the number is already negative, we know there was a number
        #Before that corresponsing to that position, therefore set that index to -1
        for i in range(len(nums)):
            if(nums[i] > 0 and nums[i] < len(nums)+1): nums[nums[i]-1] = -1*nums[nums[i]-1]
            elif(nums[i] <= 0 and -1*nums[i] < len(nums)+1): nums[-1*nums[i]-1] = -1*nums[-1*nums[i]-1] #Run step 1 and ignore negative
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0: return i+1
        
        return len(nums) + 1
    
    #NOTE: for num in nums, num = x isn't destructive

#EZ mode solution using a hash set
#However, takes O(N) space to run...
class SolutionEZ: #(O(N) time, O(N) space)
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums) #O(N)
        ans = 1
        while ans in numSet:
            ans += 1
        return ans