class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        elif n == 1:
            return s

        maxLen = 1
        maxLenIndicies = (0,0)

        for i in range(n):
            # Check the odd and even length palindromes

            # Odd palindromes first
            l,r = i-1,i+1
            currLen = 1
            currIndicies = (l, r)
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    currLen += 2
                    currIndicies = (l,r)
                    l -= 1
                    r += 1
                else:
                    break
            
            if currLen > maxLen:
                maxLen = currLen
                maxLenIndicies = (currIndicies[0], currIndicies[1]) 

            currLen = 0
            l,r = i,i+1
            currIndicies = (l, r)
            # Check even palindrome
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    currLen += 2
                    currIndicies = (l, r)
                    l -= 1
                    r += 1
                else:
                    break

            if currLen > maxLen:
               maxLen = currLen
               maxLenIndicies = (currIndicies[0], currIndicies[1]) 
        
        return s[maxLenIndicies[0]:maxLenIndicies[1] + 1]