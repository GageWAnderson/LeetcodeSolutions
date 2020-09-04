#Brute force is to use backtracking and try all solutions
#Memoize that recursion and bring down the complexity
#Find all unique is making me think DP immediately

#These solutions are far to easy for DFS, need a O(n^2) solution
class SolutionDFS:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        seenQuads = set()
        
        def dfs(L,depth,curr,currSum):
            if depth == 4:
                if currSum == target:
                    seenQuads.add(tuple(curr))
                return
            else:
                for i in range(len(L)):
                    newList = L[:i]+L[i+1:]
                    curr.append(L[i])
                    dfs(newList,depth+1,curr,currSum+L[i])
                    curr.pop()
        
        dfs(nums,0,[],0)
        seenQuads = list(seenQuads)
        return [list(res) for res in seenQuads]