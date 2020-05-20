#Find the breakpoint between the section of larger numbers that comes first
#And the section of smaller numbers that comes second with binsearch O(log(n))

#If the value being searched is greater than the pivot, binsearch on the left partition O(log(n))
#If the value being searched is less than the pivot, binsearch on the right partition
#If the value being searched is equal to the partition, return the index

#Also, if you can be destructive to the array, once you find the break-point index you can just
#Un-rotate the array (This takes too much time since it is O(N))

#Struggling with the edge cases of binary search (as expected), need to look at the solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 0): return -1 #Clean up the input
        
        lower, upper = 0, len(nums) -1 #need upper index to be in bounds
        
        while lower != upper:
            mdpt = lower + (upper - lower)//2
            
            if nums[lower] < nums[upper]: #Do binary search because it conditions are met
                if target > nums[mdpt]: lower = mdpt + 1
                else: upper = mdpt
                    
            else: #Need to get to the place where we can do binary search
            #There are 4 possible regions where the midpoint can be, change bounds depending on the region so you can binsearch
                if nums[mdpt] < nums[upper]: #need >= here in case we found the answer
                    if target > nums[mdpt] and target <= nums[upper]: lower = mdpt + 1
                    else: upper = mdpt
                else:
                    if target >= nums[lower] and target <= nums[mdpt]:upper = mdpt
                    else: lower = mdpt + 1
                     
        if nums[lower] == target: return lower
        else: return -1
                
    
    #Again, binary search is pretty easy to implement, I was overthinking this problem
        
        #first binary search sets the breakPointIndex to some value 0<breakPointIndex<len(nums)
        #you know you are at this index when the value on the right of the index (breakPointIndex + 1) is greater than
        #nums[breakPointIndex]
            #OPTIMIZATION: If you happen to find target here, just return i
            
        #If breakPointIndex is still -1, just do regular binsearch to find target
        
        #second binary search looks at the left, right sides of [0,breakPointIndex -1] or [breakPointIndex + 1, len(nums)-1]
        #Return i as soon as you find target