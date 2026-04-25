class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        print(f"s = {s}")
        if s in self.memo:
            return self.memo[s]
        elif not s or len(s) == 0:
            self.memo[s] = False
            return False
        elif s in wordDict:
            return True
        
        for i in range(len(s)):
            print(s[:i])
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                self.memo[s] = True
                return True
        
        self.memo[s] = False
        return False

class SolutionTopDown:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in self.memo:
            return self.memo[s]
        elif len(s) == 0:
            return True
        
        for word in wordDict:
            if len(word) <= len(s) and s[:len(word)] == word:
                if self.wordBreak(s[len(word):], wordDict):
                    self.memo[s] = True
                    return True
        
        self.memo[s] = False
        return False

class SolutionBottomUp: # Done by going backwards and using a dp[] to memoize

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True

        for i in range(len(dp) - 2, -1, -1):
            for word in wordDict:
                if len(word) <= len(dp) - i - 1 and s[i:i + len(word)] == word:
                    if dp[i + len(word)]:
                        dp[i] = True
        
        print(dp)
        return dp[0]