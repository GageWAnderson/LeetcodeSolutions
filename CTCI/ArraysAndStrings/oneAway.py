#Case 1: s1,s2 are the same size, only worry about replace
#Case 2: One is larger than the other (Insertion/deletion are the same 
#               if you just reverse what string you are looking at)
    #If one is more than 1 character longer than the other
    #Return false immediately
    #Smaller substring is 1 or 2 contiguous substrings within the larget string

def oneAway(s1,s2):
    m,n = len(s1),len(s2)
    if abs(m - n) > 1: return False

    if m > n: #Switch so s1,m are always the smaller one
        m,n = n,m
        s1,s2 = s2,s1

    if m == n: #Check the replacement step
        numDiff = 0
        for i in range(m):
            if numDiff > 1: return False
            if s1[i] != s2[i]: numDiff += 1
        return True #Return true on zero edits as well

    elif m == n - 1: #Check the insertion/removal steps
        if s2[0] != s1[0]: return s1 == s2[1:n]
        elif s2[n-1] != s1[m-1]: return s1 == s2[0:n-1]
        else:
            point = 0
            for i in range(n-1):
                if s2[i] != s1[i]: 
                    point = i
                    break #Have to break here else point is reset
            return (s1[0:point] == s2[0:point] and s1[point:m] == s2[point+1:n])
    return False

if __name__ == "__main__":
    print(oneAway("ple","pale"))
    print(oneAway("pales","pale"))
    print(oneAway("pale","bale"))
    print(oneAway("pale","bake"))

#Solution notes:
#This is one of those problems where it is helpful to think of the meaning of each
#Operation

#Replacement: Means that strings are the same length and differ in one place
#Insertion: Strings are identical, except for a shift at some point in the strings
#Removal: The inverse of insertion