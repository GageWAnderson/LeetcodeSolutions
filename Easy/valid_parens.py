class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chars = ["(", "[", "{"]
        close_chars = [")", "]", "}"]
        valid_pairs = {"(": ")", "[": "]", "{": "}"}

        for i in range(len(s)):
            if s[i] in open_chars:
                stack.append(s[i])
            elif s[i] in close_chars:
                if not stack or valid_pairs[stack[-1]] != s[i]:
                    return False
                stack.pop()
            else:
                raise ValueError("Only open, close chars in string")
        return not stack
