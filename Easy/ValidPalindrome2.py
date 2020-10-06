class Solution: #This question could benefit from some recursion
    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp1 = s[:l]+s[l+1:]
                tmp2 = s[:r]+s[r+1:]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
        return True