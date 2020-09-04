#Just loop through the word and see if the segment is in the wordDict
#This is too simple, need to backtrack and try another combonation if a given
#Choice fails
class SolutionRecursiveSlow: #This brute force is O(2^n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict) #Same word can be used twice
        
        def helper(s):
            if s in words:
                return True
            elif s in memo:
                return memo[s]
            else:
                for i in range(len(s)):
                    if s[:i+1] in words and helper(s[i+1:]):
                        return True
                return False
        
        return helper(s)

#Just loop through the word and see if the segment is in the wordDict
#This is too simple, need to backtrack and try another combonation if a given
#Choice fails
class SolutionMemoizationFast: #The Memoized DP is O(n^2)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict) #Same word can be used twice
        memo = dict() #Forgot about recursive memoization, reduces this problem to O(n^2)
        
        def helper(s):
            if s in words:
                return True
            elif s in memo:
                return memo[s]
            else:
                for i in range(len(s)):
                    if s[:i+1] in words and helper(s[i+1:]):
                        memo[s] = True
                        return True
                    memo[s] = False
                return False
        
        return helper(s)

#There is also a DFS solution to this problem