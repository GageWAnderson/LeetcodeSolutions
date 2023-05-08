class SolutionDFS:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        
        seen = set()

        def dfs(node):
            if node == len(nums) - 1:
                return True
            elif node >= len(nums):
                return False # Out of bounds
            
            seen.add(node)
            for nbor in getNbors(node):
                if nbor not in seen and dfs(nbor):
                    return True
            return False
        
        def getNbors(node):
            res = []
            if nums[node] == 0:
                return res
            
            for i in range(1, nums[node] + 1):
                if (node + i) < len(nums):
                    res.append(node + i)
            return reversed(res)
        
        return dfs(0)

class SolutionGreedy:
    def canJump(self, nums: list[int]) -> bool:
        lastGoodPosition = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if (i + nums[i] >= lastGoodPosition):
                lastGoodPosition = i
        return lastGoodPosition == 0