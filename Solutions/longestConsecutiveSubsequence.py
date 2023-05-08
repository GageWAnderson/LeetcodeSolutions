class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxSeqLength = 1
        numSet = set(nums) # O(n)
        
        for num in nums:
            if num not in numSet:
                continue
            
            i,j = 1,1
            currSeqLength = 1
            while True:
                if (num + i) not in numSet and (num - j) not in numSet:
                    maxSeqLength = max(maxSeqLength, currSeqLength)
                    numSet.remove(num)
                    break

                if (num + i) in numSet:
                    numSet.remove(num + i)
                    i += 1
                    currSeqLength += 1
                if (num - j) in numSet:
                    numSet.remove(num - j)
                    j += 1
                    currSeqLength += 1
        
        return maxSeqLength