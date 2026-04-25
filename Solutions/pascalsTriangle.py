import copy
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        prev_row = [1]
        for row in range(1, numRows):
            curr_row = [1 for _ in range(len(prev_row) + 1)]
            for i in range(1, len(curr_row) - 1):
                curr_row[i] = prev_row[i-1] + prev_row[i]
            res.append(curr_row) 
            prev_row = copy.deepcopy(curr_row)

        return res

import copy
class SolutionRecursive:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        def pascal(row_num):
            if row_num == 1:
                res.append([1])
                return [1]
 
            prev_row = pascal(row_num - 1)
            curr_row = [1 for _ in range(len(prev_row) + 1)]
            for i in range(1, len(curr_row) - 1):
                curr_row[i] = prev_row[i - 1] + prev_row[i]
            res.append(curr_row)
            return curr_row
        
        pascal(numRows)
        return res