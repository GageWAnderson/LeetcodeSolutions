class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            res += 1 # Every letter is its own palindrome

            # Odd length palindrome centered on i
            l,r = i-1,i+1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
            
            # Even length palindrome centered on i and i + 1
            l,r = i,i+1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        return res