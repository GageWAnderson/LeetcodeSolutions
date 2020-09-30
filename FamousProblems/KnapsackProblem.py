class KnapSackProblem:
    #Consider all possible weights from 1 to W (columns)
    #Rows are the possible items to put into the bag
    def knapSack(self,vals,weights,capacity):
        dp = [[0 for x in range(capacity + 1)] for x in range(len())]
        n = len(vals)

        #Build DP table from the bottom-up O(n^2)
        for i in range(n+1):
            for w in range(capacity+1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif weights[i-1] <= w:
                    dp[i][w] = max(vals[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[i][capacity]
                