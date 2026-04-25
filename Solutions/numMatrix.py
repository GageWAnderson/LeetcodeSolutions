class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS,COLS = len(matrix), len(matrix[0])
        self.cumulative_sum_matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)] #(O(mn)) space

        for row in range(ROWS):
            for col in range(COLS):
                up = self.cumulative_sum_matrix[row - 1][col] if row > 0 else 0
                right = self.cumulative_sum_matrix[row][col - 1] if col > 0 else 0
                up_and_right = self.cumulative_sum_matrix[row - 1][col - 1] if row > 0 and col > 0 else 0
                self.cumulative_sum_matrix[row][col] = matrix[row][col] + up + right - up_and_right

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        large_rect = self.cumulative_sum_matrix[row2][col2]
        up_rect = self.cumulative_sum_matrix[row1 - 1][col2] if row1 > 0 else 0
        right_rect = self.cumulative_sum_matrix[row2][col1 - 1] if col1 > 0 else 0
        up_right_rect = self.cumulative_sum_matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        
        return large_rect - up_rect - right_rect + up_right_rect # O(1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)