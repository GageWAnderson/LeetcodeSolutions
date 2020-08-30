#Use layer variable to keep track of where to stop when spiraling in the matrix
#Increment layer starting at 0 when you move left into the next inner layer
#Right,down,left,up -> up direction has one less distance then go right again and increment layer
class SolutionSimulationBad:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []: return []
        m,n = len(matrix),len(matrix[0])
        if n == 0: return []
        if n == 1: return [matrix[0][0]]
        layer = 0
        count = 0
        res = []
        i,j = 0,0
        
        while count < m*n and count < m*n:
            while j+layer < n and count < m*n:
                res.append(matrix[i][j])
                j += 1
                count += 1
                if count >= m*n: break
            i += 1
            j -= 1
            while i+layer < m and count < m*n:
                res.append(matrix[i][j])
                i += 1
                count += 1
            j -= 1
            i -= 1
            while j-layer >= 0 and count < m*n:
                res.append(matrix[i][j])
                j -= 1
                count += 1
            i -= 1
            j += 1
            while i-layer-1 >= 0 and count < m*n:
                res.append(matrix[i][j])
                i -= 1
                count += 1
            i += 1
            j += 1 #Go left at end of cycle
            layer += 1
            print(f"count = {count}")
        return res