#Alberto gave me the optimal solution, however I was on track
#For the less-optimal solution before that
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #Use a string-builder to build up the answer
        #Goal is to correct the innermost invalid paren and return the string in order otherwise
        removed = set()
        parenCount = 0
        unclosed = []
        
        for i in range(len(s)):
            if s[i] == "(":
                unclosed.append(i)
                parenCount += 1
            elif s[i] == ")":
                parenCount -= 1
                if unclosed: #Forgot this line
                    unclosed.pop()
            
            if parenCount < 0:
                removed.add(i)
                parenCount += 1 #Forgot this
        
        uc = set(unclosed)
        sb = []
        for i in range(len(s)):
            if i not in removed and i not in uc:
                sb.append(s[i])
        return "".join(sb)