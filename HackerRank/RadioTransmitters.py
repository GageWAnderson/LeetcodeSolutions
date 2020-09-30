def hackerlandRadioTransmitters(x, k):
    n = len(x)
    if n == 1: return 1
    x.sort() #O(nlogn)
    i = 0 #i marks the start of a given range
    res = 0

    while i < n:
        res += 1
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
        loc = x[i-1] + k
        while i < n and x[i] <= loc:
            i += 1
    return res
    
    return res

#This is a dp-esque greedy O(n) solution