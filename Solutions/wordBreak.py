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