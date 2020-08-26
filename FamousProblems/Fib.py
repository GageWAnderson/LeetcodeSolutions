class Solution:
    def __init__(self):
        self.dp = dict()

    def fib(self,n): #Gets the nth fib number, O(n) with DP
        if n in self.dp.keys():
            return self.dp[n]
        if n == 0: return 0
        elif n == 1: return 1
        else:
            res = self.fib(n-1) + self.fib(n-2)
            self.dp[n] = res
            return res