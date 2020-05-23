#CTCI 1.9
#Find the first point of difference and use isSubstring on s3
#Just create a new string s3 in the correct 

def stringRotation(s1,s2):
    m,n = len(s1),len(s2)
    if m != n: return False
    point = 0 #breakpoint is a keyword you can't use
    for i in range(m):
        if s1[i] != s2[i]: point = i
    s3 = s1[i:m] + s1[0:i]
    return isSubstring(s2,s3)