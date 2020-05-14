class SolutionSlow: #Runs in O(n^3) time
    #I tried dynamic programming here, but my solution was still really slow...
    #The optimizations I made did not prevent the solution from being O(n^3)
    def isPalindrome(self, s:str, pals):
        i = 0
        j = len(s) - 1
        #print(f"i = {i}, j= {j}")
        
        if(i == j): return True #Checks singles
        elif(j == i+1): #Checks doubles
            return s[i] == s[j]
        elif(s in pals): return True #DP shortcut
        else:
            if(s[i] == s[j] and self.isPalindrome(s[i+1:j],pals)):
                pals.add(s)
                return True
            return False
    
    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)
        maxLen = 0
        max = ""
        
        if(j == 1): return s
        pals = set() #Store known palindromes for dynamic programming
        
        for i in range(0, len(s) - 1): #This nested loop is O(n^3)
            j = len(s)
            if(j-i < maxLen): break
            while(j-i > maxLen and i != j):
                if(j-i > maxLen and self.isPalindrome(s[i:j],pals)):
                    max = s[i:j]
                    maxLen = j-i
                j -= 1
        return max
        
#Better solution, uses expanding in both directions to get O(n^2) time!
#Learned a lot about python strings on this problem...
#Also, the two cases (even vs. odd palindrome lengths) made this problem significantly harder
def expandFromChar(s: str, i: int):
    p1 = i - 1
    p2 = i + 1 #Start by looking at string of length 3
    if(i <= 0 or i >= len(s) -1): return 1
    stop = False
    strLen = 1 #len is a reserved word, don't name your variables len,
    #also start at single-character palindrome length of 1
    while(not stop and p1 >= 0 and p2 <= len(s) -1):
        if(s[p1] == s[p2]):
            strLen += 2
            p1 -= 1
            p2 += 1
        else:
            stop = True
    return strLen

def expandFromMid(s:str, i: int):
    lo = i
    hi = i +1
    if(i < 0 or i >= len(s) -1): return 1
    strLen = 0 #len is a reserved word, don't name your variables len
    while(lo >=0 and hi <= len(s) -1):
        if(s[lo] != s[hi]): return strLen
        else:
            strLen += 2
            lo -= 1
            hi += 1
    return strLen
        
class SolutionBetter: #O(n^2)
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxPal = ""
        if(len(s) == 0): return maxPal
        if(len(s) == 1): return s
        for i in range(0,len(s)-1):
            len1 = expandFromChar(s,i)
            len2 = expandFromMid(s,i) #looks at the point between s[i] and s[i+1] 
            print(f"len1 = {len1}, len2={len2}")
            
            if(len1 > len2 and len1 > maxLen):
                maxLen = len1
                maxPal = s[i-len1//2:i+len1//2+1] #String slicing is right-exclusive in python
            if(len1 <= len2 and len2 > maxLen):
                maxLen = len2
                maxPal = s[i-len2//2+1:i+len2//2+1]
        return maxPal