class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""

        for i in range(len(s)):
            left,right = i - 1, i + 1
            odd_palindrome_length = 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    odd_palindrome_length += 2
                    left -= 1
                    right += 1
                else:
                    break
            if odd_palindrome_length > len(longest_palindrome):
                longest_palindrome = s[left+1:right]

            left,right = i, i + 1
            even_palindrome_length = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    even_palindrome_length += 2
                    left -= 1
                    right += 1
                else:
                    break
            if even_palindrome_length > len(longest_palindrome):
                longest_palindrome = s[left+1:right]
        
        return longest_palindrome # O(N^2) time, O(1) space