class Solution:
    def myAtoi(self, str: str) -> int:
        num = 0 #value to return
        negative = False
        s = str
        i = 0
        intMax = 2**31 -1
        intMin = -2**31
        
        if(len(s) == 0): return 0
        
        while s[i] == " ": #Be careful about indexing out of range on these loops!
            i+=1 #Spaces are the only allowed whitespaces
            if(i == len(s)): return 0 #Return 0 if the string is all whitespace
        if (s[i] != '+' and s[i] != '-' and not s[i].isdigit()): return 0 # be careful with the logic in these loops
        if(s[i] == '+' or s[i] == '-'): 
            if(i == len(s)-1): return 0 #only + or - is not allowed
            if(s[i] == '-'): 
                negative = True
            i += 1
        print(s[i])
        while (i < len(s) and s[i].isdigit()): #Needed to use short-circuit evaluation here...
            num *= 10
            num += (ord(s[i]) - 48) #0 is 48 in the ASCII table, a is 97
            i += 1
        if(negative): 
            num *= -1
        
        if num > intMax: return intMax
        elif num < intMin: return intMin
        else: return num
        
        #NOTE: I missed a lot of edge cases in my original coding...
        #NOTE: This question requires knowledge of the ASCII table, and
        #Lots of small edge cases to made sure are right...