#Number of ways => Dynamic Programming
# # of ways at a given point in the string = ways before + ways current
#Need to account for the fact that some larger numbers don't count so can
#Only be treated as singles

class Solution: #Was close, however missed the possibility of 0
    def numDecodings(self, s: str) -> int: #s is all digits 
        if s[0] == "0": return 0
        dp = [0 for x in range(len(s) + 1)] #Needs to be len(s) + 1 since looking at 2 elements behind to get last elem
        dp[0] = 1
        if s[0] == 0: #Didn't know 0 was a possibility here... (need to ask about this)
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2,len(s)+1):
            if int(s[i-2:i]) <= 26 and int(s[i-2:i]) >= 10: #2-digit decode possible
                dp[i] += dp[i-2] #Treating them together adds 1 double and 
            if int(s[i-1]) != 0: #Again, need to account for 0
                dp[i] += dp[i-1]
        return dp[len(s)]