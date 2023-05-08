from functools import lru_cache

"""
Need to use lru_cache to memoize the results of the recursive calls
Got this problem wrong because I didn't consider the case where the first digit is 0
or other edge cases.
"""
class Solution:

    @lru_cache(maxsize=None)
    def numDecodings(self, s: str) -> int:

        def canTake2Digits(s : str):
            sumOfFirstTwo = int(s[0] + s[1])
            return len(s) > 2 and sumOfFirstTwo >= 10 and sumOfFirstTwo <= 26

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if s[0] == "0":
                return 0
            else:
                return 1
        elif len(s) == 2:
            if s[0] == "0":
                return 0
            else:
                sumOfFirst2 = int(s[0] + s[1])
                if sumOfFirst2 > 10 and sumOfFirst2 <= 26 and sumOfFirst2 != 20:
                    return 2
                elif sumOfFirst2 == 10 or sumOfFirst2 == 20:
                    return 1
                else:
                    return self.numDecodings(s[1:])
        else:
            if s[0] == "0":
                return 0
            else:
                if canTake2Digits(s):
                    return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
                else:
                    return self.numDecodings(s[1:])