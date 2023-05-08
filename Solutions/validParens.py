class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = {')' : '(', '}': '{', ']': '['}
        openParens = set(['(', '[', '{'])
        closeParens = set([')', ']', '}'])

        for p in s:
            if p in openParens:
                stack.append(p)
            elif p in closeParens:
                if stack and stack[-1] == parenMap[p]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0