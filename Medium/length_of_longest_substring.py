class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # NOTE: Solve with the brute force, then with the more efficient solution
        if len(s) < 2:
            return len(s)
        i, j = 0, 0
        longest = 1
        seen = set()
        seen.add(s[i])
        while j < len(s) - 1:
            j += 1
            while s[j] in seen and i < j:
                # Contract the left until the duplicate is removed
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            longest = max(longest, j - i + 1)

        return longest


# Example s="a", ans = 1, s="", ans = 0 correct
# Example s="bb", ans = 1
# Example s="abcabcbb"
# Greater than len 2 so go to body
