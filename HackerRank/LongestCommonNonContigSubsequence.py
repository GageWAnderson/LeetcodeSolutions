# Complete the commonChild function below.
# Output is an int of the longest common child
# Strings are equal length (this makes it easier)
# This is a longest common subsequence problem

# Suppose that two sequences both end in the same element. Then their LCS is the LCS of the sequence with the last element excluded, with the common last element appended.
def commonChild(s1, s2):
    if len(s1) == 1:
        return 1 if s1[0] == s2[0] else 0
    dp = [[0 for j in range(len(s2)+1)] for i in range(2)] #first 2 rows
    for i in range(1,len(s1)+1): #DP table starts w/ empty string
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[1][j] = dp[0][j-1] + 1
            else:
                dp[1][j] += max(dp[0][j],dp[1][j-1])
        dp[0] = copy.deepcopy(dp[1])
        dp[1] = [0]*(len(s2)+1)
    print(dp)
    return dp[0][-1]