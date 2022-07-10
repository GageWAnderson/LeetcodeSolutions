class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        
        ranges = []
        currRangeStart = nums[0]
        currRangeEnd = nums[0]
        for i,num in enumerate(nums):
            if i > 0 and num != currRangeEnd + 1:
                if currRangeStart == currRangeEnd:
                    ranges.append(str(currRangeStart))
                else:
                    ranges.append(f"{currRangeStart}->{currRangeEnd}")
                currRangeStart = num
            currRangeEnd = num
        
        if currRangeStart == currRangeEnd:
            ranges.append(str(currRangeStart))
        else:
            ranges.append(f"{currRangeStart}->{currRangeEnd}")
        
        return ranges