class Solution:
    def notInRange(self,x: int):
        #Checks that x is in the proper range
        intMin = -2**31
        intMax = 2**31 -1
        print(x < intMin and x > intMax)
        return x < intMin or x > intMax
    
    def reverse(self, x: int) -> int:
        y = 0
        isNegative = x < 0
        if(isNegative): x *= -1
        while(x != 0): 
            z = x%10
            y = y*10
            y += z
            x = x//10
            if(self.notInRange(x) or self.notInRange(y)): return 0
        if(isNegative): y*= -1
        return y
    

    #Notes:
    #Need to pass self between helper functions so you can always have access to
    #the helper functions in the same class
    #** is the power operator in python
    #Need to use the // operator for integer division
    #Need to control for negative numbers because % has different behavior with negatives
    
    #Final error, was checking for overflow first, when I needed to check for it after y had been modified