class Solution:
    def isUnique(self,s): #O(N) time, O(N) space
        seen = set()
        for char in s:
            if char in seen: return False
            seen.add(char)
        return True

    #You can do this the hard way with pointers if you
    #Don't have access to a hash set (maybe?!)

def hash(s): #O(S)
    res = 0
    count = 0
    for char in s: #s is the smaller string
        res += ord(char)*128**count #Rabin Fingerprint Hash (good hash fxn)
        count += 1
    return res

def existsSubstring(s,b): #O(N) time, O(1) space (in-place)
    #Use Rabin-Karp Substring search to find Substrings in Linear time in O(1) space! (CTCT Pg. 636)
    #This comes up a lot in interviews, makes looking for substrings efficient
    #Page 90
    val = hash(s)  #O(S)
    seg = hash(b[0:len(s)]) #O(S)
    #O(B - S)
    if(seg == val): return True #Edge case where both are the same length
    for i in range(len(b)-len(s)): #Loop through b, no sequence of length s can have a hash of val O(B)
        if seg == val: return True
        else:
            seg -= hash(b[i])
            seg += hash(b[i + len(s)])
    return False
            


if __name__ == "__main__":
    Sol = existsSubstring("helloworld","helloworld")
    print(Sol)