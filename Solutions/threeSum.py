class SolutionWithSorting:
    """
    Addressing several question regarding the "No-Sort" approach. 
    We recommend approach 1 for interviews, and approach 3 (No-Sort) is to address a possible follow-up question 
    (e.g. "what if you cannot sort the array"). The point here is that it's possible, though the 
    efficiency would heavily depend on the input. If we have a very large array 
    with many duplicates and a few matching triplets, the "No-Sort" approach would be more memory efficient.
    Figuring out and communicating pros and cons of each approach is very important during an interview.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def twoSum(arr, target):
            if len(arr) < 2:
                return

            l,r = 0,len(arr) - 1

            while l < r:
                if arr[l] + arr[r] == target:
                    res.append([arr[l], arr[r], -target])
                    l += 1
                    r -= 1
                    while l < len(arr) - 1 and arr[l] == arr[l - 1]:
                        l += 1
                    while r >= 0 and arr[r] == arr[r + 1]:
                        r -= 1 # Skip duplicates
                elif arr[l] + arr[r] < target:
                    l += 1
                    while l < len(arr) - 1 and arr[l] == arr[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while r >= 0 and arr[r] == arr[r + 1]:
                        r -= 1 # Skip duplicates
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                twoSum(nums[i+1:], -nums[i])
        
        return res