class SolutionBad: # O(len(coins)^n), very slow runtime
    #Find the total number of ways to make
    #Change for n cents with a given selection of coins (in an array)
    def coinChange(self,coins,n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if len(coins) == 0 and n >= 1:
            return 0
        return self.coinChange(coins[:len(coins)-1],n) + self.coinChange(coins,n-coins[-1])

#Like other typical Dynamic Programming problems, re-computations of same sub-problems
#Is avoided by constructing a temporary array dp[][] bottom-up
class SolutionGood: #O(len(coins)*n), Better Solution using DP
    def coinChange(self,coins,n):
        m = len(coins)
        table = [[0 for i in range(n+1)] for j in range(m+1)]
        #Fill in the squares we know in the table
        table[0][0] = 1
        for i in range(1,n+1):
            table[0][i] = 0
        for j in range(1,m+1):
            table[j][0] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                a = table[i - coins[j]][j] if i - coins[j] >= 0 else 0
                b = table[i][j-1] if j >= 1 else 0
                table[i][j] = a + b
        
        return table[n][m]

class SolutionBest: #O(n) space, rather than O(n*len(coins)) space
    def coinChange(self,coins,n):
        m = len(coins)
        table = [0 for k in range(n+1)]
        table[0] = 1
        for i in range(0,m):
            for j in range(coins[i],n+1):
                table[j] += table[j-coins[i]]
        return table[n]





#The bad soluiton is recursive, the DP good solution is iterative and uglier...
#This might be an upcoming DP pattern

#The key is to see problem as a table with each square a solution to a partial problem
#Then, build the solution up from the table