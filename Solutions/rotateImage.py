class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = matrix
        n = len(m)
        layer = 0

        while layer < n // 2:
            for i in range(n // 2 + n % 2): # Got this line wrong, ran too many times
                upperLeft = m[layer][i]
                upperRight = m[i][n-layer-1]
                lowerRight = m[n-layer-1][n-i-1]
                lowerLeft = m[n-1-i][layer] # math on 4 squares to switch was correct

                m[layer][i] = lowerLeft
                m[i][n-layer-1] = upperLeft
                m[n-layer-1][n-i-1] = upperRight
                m[n-1-i][layer] = lowerRight
            
            layer += 1