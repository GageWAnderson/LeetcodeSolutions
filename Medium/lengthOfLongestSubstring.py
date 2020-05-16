class SolutionBad: #Runs in O(n^2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubst = ""
        maxLen = 0
        for i in range(len(s)):
            seen = set()
            currLen = 1 #Naming variables len is not allowed!
            j = i
            seen.add(s[j])
            while(j < len(s) -1):
                j += 1
                if(s[j] in seen): break
                currLen += 1
                seen.add(s[j])
            if(currLen > maxLen):
                maxLen = currLen
                maxSubst = s[i:currLen]
            if(maxLen >= (len(s) - i - 1)): 
                    break #Optimization, we are done if the length of the longest substring is greater than the number of remaining chars
        return maxLen
        
        #Got the hash set, however missed the sliding window, giving O(n^2) time
        #You can do this in O(n) if you simply have i skip the sections without repeats
        #Therefore, every letter is only 'touched' by i or j once, so O(n)

class SolutionBetter: #Runs in O(n), uses sliding window method with a hash set for lookups
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0): return 0
        if(len(s) == 1): return 1
        (i,j) = (0,1) #Use this syntax to declare multiple constants on the same line
        (maxLen,currLen) = (1,1)
        seen = set()
        seen.add(s[i])
        while(i < len(s) and j<len(s)):
            print(f"i = {i}, j = {j}")
            if(s[j] in seen):
                seen.remove(s[i])
                i += 1
                seen.add(s[i]) #need to account for duplicates that are right next to one another (hidden edge case)
                if(i == j): #don't move j, just move the window
                    j += 1
                currLen = j - i
            else:
                seen.add(s[j])
                j += 1
                currLen += 1
            print(f"currLen = {currLen}")
                
            if(currLen > maxLen):
                    maxLen = currLen
        return maxLen