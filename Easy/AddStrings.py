#This problem is grade-school addition in a computer
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = 0
        res = [] #String-builder DS, will join this to make the result at the end
        num1 = num1[::-1]
        num2 = num2[::-1] #Needed to reverse the input for grade-school math
        if len(num1) < len(num2): num1,num2 = num2,num1 #Num1 is always longer
            
        while i < len(num2):
            n1 = int(num1[i])
            n2 = int(num2[i]) #Don't feel like memorizing ASCII codes...
            num = n1 + n2 + carry
            if num >= 10:
                res.append(str(num%10))
                carry = 1
            else:
                res.append(str(num))
                carry = 0
            i += 1
            
        if i == len(num1) and carry == 1:
            res.append(str(carry))
        elif i < len(num1):
            for j in range(i,len(num1)):
                n = int(num1[j])
                if n + carry >= 10:
                    res.append(str((n + carry)%10))
                    carry = 1
                else:
                    res.append(str(n + carry))
                    carry = 0
            if carry == 1:
                res.append(str(carry))
                
        res.reverse()    
        return "".join(res)