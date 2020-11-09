import heapq
class SolutionDjikstraReference: #O(ElogV)
    def minPathSum(self, grid: List[List[int]]) -> int:
        def path_sum(grid, parent, node):
            s = 0
            while node != (0,0):
                i, j = node
                s += grid[i][j]
                node = parent[node]

            s += grid[0][0]
            return s

        def moves(M, N, node):
            i, j = node
            nxt = []
            if i + 1 < M:
                nxt += [(i+1, j)]

            if j + 1 < N:
                nxt += [(i, j+1)]

            return nxt

        def h_n(M, N, node):
            i, j = node
            return max(
                abs(M-i),
                abs(N-j)
            )
    
        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])
        
        seen = set()
        start = (0,0)
        dist = {start: grid[0][0]}
        parent = {}
        explore = []
        heapq.heappush(explore, (0, start))
        
        while len(explore) > 0:
            _, node = heapq.heappop(explore)
            if node in seen:
                continue
            elif node == (M-1, N-1):
                return path_sum(grid, parent, node)
            else:
                seen.add(node)
                
            for move in moves(M, N, node):
                i, j = node
                g_n = dist[node] + grid[i][j]
                f_n = g_n
                heapq.heappush(explore, (f_n, move))
                if move not in dist or g_n < dist[move]:
                    dist[move] = g_n
                    parent[move] = node
                    
        return -1

class DjikstraSolutionAttempt:
        def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if m == 0 or n == 0: return -1
        
        dists = [inf for x in range(m*n)]
        dists[0] = 0
        minHeap = []
        entries = {} 
        
        def getNbors(u):
            res = []
            row = u // n
            col = u % n
            if row < m-1: #Down
                res.append(u + n)
            if col < n-1:
                res.append(u + 1)
            return res

        def getMin(heap):
            while heap:
                top = heapq.heappop(heap)
                if top[1] != -1:
                    del entries[top[1]]
                    return top
            return None

        def changeEntry(heap,v,dist):
            if v in entries.keys():
                entries[v] = -1 #Remove node
            newNode = [dists[v],v]
            heapq.heappush(minHeap,newNode)
            entries[v] = dist
        
        #Make the minHeap
        for i in range(m):
            for j in range(n):
                node = m*i + j
                newEntry = [inf,node]
                if i == 0 and j == 0:
                    newEntry[0] = 0 #Start node has distance of 0
                heapq.heappush(minHeap,newEntry)
                entries[node] = newEntry[0]
        
        while minHeap:
            newNode = getMin(minHeap)
            u = newNode[1]
            if u == -1: continue #Removed node
            print(f"node = {newNode}, nbors = {getNbors(u)}")
            for v in getNbors(u):
                i,j = v // n, v % n
                if v in entries.keys() and dists[u] != inf and \
                grid[i][j] + dists[u] < dists[v]:
                    dists[v] = grid[i][j] + dists[u]
                    changeEntry(minHeap,v,dists[v])
        print(f"dists = {dists}")
        return dists[-1]


class SolutionDPBasic: #O(mn), O(mn) space, can reduce space requirements
#Can get solution in constant space if matrix can be modified (should ask this in interview)
#Recursive Solution is O(2^(m+n))
#DP solution is O(mn), O(mn) space that can be reduced
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if m == 0 or n == 0: return 0
        dpGrid = [[-1 for x in range(n)] for y in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    dpGrid[i][j] = grid[i][j]
                elif j == n-1 and i != m-1:
                    dpGrid[i][j] = grid[i][j] + dpGrid[i+1][j]
                elif j != n-1 and i == m-1:
                    dpGrid[i][j] = grid[i][j] + dpGrid[i][j+1]
                else:
                    dpGrid[i][j] = grid[i][j] + min(dpGrid[i+1][j], dpGrid[i][j+1])
        return dpGrid[0][0]


#EZ DP solution when coming back to the problem
#This is memory-optimal since you can be destructive of the input
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        
        for j in range(1,n):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1,m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
                
        return grid[-1][-1]