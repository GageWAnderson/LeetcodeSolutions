class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+","-","*","/"}
        for token in tokens:
            if token in ops:
                top = stack.pop()
                second = stack.pop() #Assumes sequence is well-formed
                if token == "+":
                    stack.append(top+second)
                elif token == "-":
                    stack.append(second-top)
                elif token == "*":
                    stack.append(second*top)
                elif token == "/":
                    if second*top < 0:
                        #Make sure division with negatives rounds to 0
                        stack.append(-1*(abs(second)//abs(top)))
                    else:
                        stack.append(second//top) #Don't forget to use integer division
                    #Integer division does'nt round to 0 for negative numbers
            else:
                stack.append(int(token))
        return stack.pop()