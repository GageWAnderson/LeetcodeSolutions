    #This is a lot like is valid, but you keep track of the length of the stack, maximum length,
    #And reset the stack when you find and invalid paren
    #This problem was too hard, needed to look at the answer (MY IDEA OF USING A STACK WAS RIGHT)
    #Starting by pushing -1 onto the stack was fairly difficult...
    
class Solution: #Copied the answer, super clean I want to be able to write python like this...
    def longestValidParentheses(self, s: str) -> int:
        stack, curr_longest, max_longest = [], 0, 0
        for c in s:
            if c == '(':
                stack.append(curr_longest)
                curr_longest = 0
            elif c == ')':
                if stack:
                    curr_longest += stack.pop() + 2
                    max_longest = max(max_longest, curr_longest)
                else:
                    curr_longest = 0
        return max_longest

class MySolution: #Similar to above
    def longestValidParentheses(self, s: str) -> int:
        currLen, maxLen = 0,0
        stack = []
        
        for p in s:
            if p == '(':
                stack.append(currLen)
                currLen = 0 #forgot this line
            else:
                if stack: #makes sure stack is non-empty
                    currLen += stack.pop() + 2 #Putting lengths on the stack is more useful than strings!
                    #Need to do the following line only when currLen is updated 
                    if(currLen > maxLen): maxLen = currLen #Change the max as soon as currLen is updated
                else:
                    currLen = 0
        return maxLen