#This one was pretty easy, however I missed the case where you check the stack at the end and return false if it isn't empty...
class Solution:
    #Use a stack to keep track of the open parens!
    #Need to account for the case where there is only openers!
    def isValid(self, s: str) -> bool:
        openers = ['(','{','[']
        closers = [')','}',']']
        matches = ['()','{}','[]']
        stack = [] #Python list methods let you use them like stacks
        
        for i in range(len(s)):
            if(s[i] in openers):
                stack.append(s[i]) #push the paren onto the stack stack not, openers!
            elif(s[i] in closers and len(stack) > 0):
                opener = stack.pop()
                if(opener + s[i] not in matches): return False
            else:
                return False
        if(len(stack) == 0): return True #Don't forget to write the final return statement!!!
        else: return False #Unclosed openers should lead to returning false...
        