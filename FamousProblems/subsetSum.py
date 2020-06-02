#Variant of the following problem, solved through dynamic programming:
#https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

def subsetSum(L,sum):
    n = len(L)
    print(f"L = {L}, sum = {sum}")
    if(n == 0):
        if(sum == 0):
            return []
        else:
            return None
#you cannot return list(S[-1]).extend(rec(S[:-1])) due to it being a NoneType (it's a method call rather than an object)
    else:
        x = L[0] # [x].append(y) will return None
        if (x == sum):
            return [x]
        
        s1 = subsetSum(L[1:n],sum-x) #Slice L[1:n] not L[1,n]
        if s1:
            return [x] + s1
        else:
            s2 = subsetSum(L[1:n],sum)
            if s2:
                return [x] + s2
            return None

if __name__ == "__main__":
    L1 = [-1,0,5,7]
    S = subsetSum(L1,10)
    print(S)