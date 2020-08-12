#Need to BFS when you find an 'O' to make sure it isn't connected to the edge
#O(n) time
#Need to keep track 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []: return
        numRows = len(board)
        numCols = len(board[0])
        edgeConnectedOs = set() #Set of all points (Os) that are connected to edge
        if numRows < 3 or numCols < 3: return
        for row in range(1,numRows):
            for col in range(1,numCols):
                if board[row][col] == "O" and (row,col) not in edgeConnectedOs:
                    connected,edgeConnected = self.bfs(board,row,col)
                    if edgeConnected:
                        for point in connected:
                            edgeConnectedOs.add(point)
                    else:
                        for point in connected:
                            board[point[0]][point[1]] = "X"
    
    def bfs(self,board,row,col):
        queue = deque()
        queue.append((row,col))
        seen = set((row,col))
        connected = []
        edgeConnected = False
        
        while queue:
            node = queue.popleft()
            connected.append(node)
            if self.isEdge(board,node[0],node[1]):
                edgeConnected = True
                #Keep going to rule out all the other connected points
            
            if node not in seen:
                seen.add(node)
                nbors = self.getNbors(seen,board,node[0],node[1])
                for nbor in nbors:
                    queue.append(nbor)
        return connected,edgeConnected
    
    def isEdge(self,board,row,col):
        if row == 0 or col == 0:
            return True
        if row == len(board)-1 or col == len(board[0])-1:
            return True
        return False
    
    def getNbors(self,seen,board,row,col):
        dirs = [(0,1),(0,-1),(-1,0),(1,0)] #Down,Up,Left,Right
        nbors = []
        for direction in dirs:
            newRow,newCol = row + direction[0], col + direction[1]
            if (newRow,newCol) not in seen and not (newRow < 0 or newRow > len(board)-1 or newCol < 0 or newCol > len(board[0])-1):
                if board[newRow][newCol] == "O":
                    nbors.append((newRow,newCol))
        return nbors