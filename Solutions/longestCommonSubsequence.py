class SolutionRecursiveDP:
    def __init__(self):
        self.memo = {}
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if (text1, text2) in self.memo:
            return self.memo[(text1, text2)]

        if len(text1) == 0 or len(text2) == 0:
            self.memo[(text1, text2)] = 0
            return 0
        elif len(text1) == 1 and len(text2) == 1:
            res = 1 if text1 == text2 else 0
            self.memo[(text1, text2)] = res
            return res
        else:
            if text1[0] == text2[0]:
                res = 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
            else:
                res = max(self.longestCommonSubsequence(text1, text2[1:]),self.longestCommonSubsequence(text1[1:], text2))
            self.memo[(text1, text2)] = res
            return res

"""
Using a 2D Grid for DP is very effective
"""
class SolutionBottomUp:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]

class SolutionBottomUpMemoryOptimized:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        
        # The previous and current column starts with all 0's and like 
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]