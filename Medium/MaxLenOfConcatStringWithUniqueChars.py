class SolutionReference: #Uses DP, I found this pretty difficult
    def maxLength(self, arr: List[str]) -> int:

        def to_mask(s: str): #Did not get this part for fast comparison
            mask = 0
            buckets = [0] * 26
            for c in s:
                buckets[ord(c) - ord('a')] += 1
            count = 0
            for i, c in enumerate(buckets):
                if c > 1: return 0, -1
                if c != 0:
                    mask = mask | (1 << i)
                    count += 1
            return mask, count
        
        def recur(used_mask, index):
            if (used_mask, index) in dp: return dp[used_mask, index]
            if masks[index][1] == -1: return 0
            if used_mask & masks[index][0] != 0: return 0
            count = 0
            original_mask = used_mask
            used_mask = used_mask | masks[index][0]
            for j in range(index + 1, len(arr)):
                count = max(count, recur(used_mask, j))
            count += masks[index][1]
            dp[original_mask, index] = count
            return count
        
        masks = [to_mask(a) for a in arr] #O(n), makes comparison faster
        longest = 0
        dp = dict()
        return max(recur(0, i) for i in range(len(arr)))



#Brute force is to try all the combonations and record the maximum, O(n^2)

#Idea, try all combonations, keep a bit mask of all the characters you have
#Bit mask allows for fast tell of overlap between words O(1) instead of O(s)

#This is most similar to the max path to a target DP paradigm
#Here, the destination is having considered all elements in the list
#And the value is the combined length of the strings chosen

#Also similar to all/distinct DP problems, except it asks us for the best way
class SolutionBad:
    from itertools import combinations
    def maxLength(self, arr: List[str]) -> int:
        if arr == []: return 0
        combs = []
        for i in range(len(arr)):
            combs.append(list(combinations(arr,i+1)))
        flat = [y for x in combs for y in x]
        #print(flat)
        maxLen = 0
        for comb in flat:
            if self.isUnique(comb) and self.totalLen(comb) > maxLen:
                maxLen = self.totalLen(comb)
        return maxLen
    
    def isUnique(self,comb):
        letters = set()
        for word in comb:
            for letter in word:
                if letter in letters:
                    return False
                else:
                    letters.add(letter)
        return True
    
    def totalLen(self,comb):
        ans = 0
        for word in comb:
            ans += len(word)
        return ans