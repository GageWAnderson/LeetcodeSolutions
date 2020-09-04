#Brute force would be to try all the squares O(n^4)
#First instinct is an O(n^2) DFS problem
#Maximal -> DP, also you keep solving repeated sub-problems for repeated sections of the input
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #Need to check matrix[i-min][j-min] == 1 before updating the size of dp[i][j]
        #If not, just return 1 at that square
        if matrix == [] or matrix == [[]]: return 0 #Include both these bad inputs
        m,n = len(matrix),len(matrix[0])
        if m == 1: return max(matrix[0], key = lambda x:int(x))
        if n == 1: return int(max(matrix, key = lambda L:int(L[0]))[0])
        
        dp = [[0 for col in range(n)] for row in range(m)]
        
        def isSafe(i,j):
            return i >= 0 and i < m and j >= 0 and j < n
        
        maxSideLen = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if isSafe(i-1,j) and isSafe(i,j-1):
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    else:
                        dp[i][j] = 1
                    maxSideLen = max(dp[i][j],maxSideLen)
        return maxSideLen**2
    
    #dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.

# For all people wondering how you'd solve this in an interview in 30 mins - this is a fairly easy DP problem. 
# If you're confused its because the explanation jumps into the bottom-up DP solution without explaining how it got there. 
# You can never figure out a bottom-up DP solution without first figuring out a top down recursive approach. 
# If during the recursion you find you're solving the same sub-problem repeatedly ("overlapping sub-problems") - that's the first hint that its DP. 
# Next, if you find that the optimal answer for the current sub-problem is formed from the optimal answer for the overlapping sub-problems, 
# you now have found the optimal sub-structure. Its DP for sure. Typically problems involving finding the "longest/shortest/largest/smallest/maximal" 
# of something have the optimal-substructure. For example if the shortest distance from A to D is A->B->C->D, then it follows that the shortest distance from B to D is B->C->D.
# At first sight, this problem requires a DFS traversal - a dead giveaway that we need recursion. 
# And it also wants you to find the largest square. So you'd go to the first 1 and ask it, "Hey, what's the largest square of 1s that begins with you?". 
# To calculate that it needs to know the largest squares its adjacent cells can begin. 
# So, it'll ask the same question to its adjacent cells which will in turn will ask their adjacent cells and so on... 
# The cell that began the question will deduce that the largest square that begins with it is 1 + the minimum of all the values its adjacent cells returned.
# You'd then ask the same question to every 1 you find in the grid and keep track of the global maximum. 
# In doing so, you'll notice that the recursion causes many cells to be asked the same question again and again (overlapping sub-problems)- so you'd use memoization.
# The recursive solution takes O(m+n) space. From this, you can now figure out the bottom-up approach.