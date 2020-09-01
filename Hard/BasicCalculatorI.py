#Almost right, needed to reverse the input to deal with "-"
class Wrong:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.replace(" ","").strip()
        
        for i in range(len(s)):
            if s[i] == ")":
                currExp = []
                while stack and stack[-1] != "(":
                    currExp.append(stack.pop())
                stack.pop()
                currExpString = "".join(currExp)
                num = self.evalStr(currExpString)
                stack.append(num)
            else:
                stack.append(s[i])
        finalString = "".join(stack)
        return self.evalStr(finalString)
    
    def evalStr(self,s):
        i = 0
        num = 0 #Default return value
        print(s)
        while i < len(s):
            #print(f"i = {i}")
            if s[i].isdigit():
                num = int(s[i])
                i += 1
                while i < len(s) and s[i].isdigit():
                    num *= 10
                    num += int(s[i])
                    i += 1
            if s[i] == "+":
                return num + self.evalStr(s[i+1:])
            elif s[i] == "-":
                return num - self.evalStr(s[i+1:])
        return num

#Use a stack here as the most elegant solution, evaluate down the stack when
#You reach a ")" until you get to a "("
#These types of string traversal questions lend themselves cleanly to stacks
class SolutionReferece:

    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res       

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order.
                operand = (10**n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0

                if ch == '(':         
                    res = self.evaluate_expr(stack)
                    stack.pop()        

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)