#Optimal path substructure strongly implies DP solution
#I am actually more comfortable doing this with DFS

#This was correct, just needed some memoization to speed it up
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = set()
        def get_nbors(curr_stone,prev_jump):
            nbors = []
            for i in range(curr_stone+1,len(stones)):
                dist = stones[i] - stones[curr_stone]
                if dist >= prev_jump-1 and dist <= prev_jump+1:
                    nbors.append(i)
                elif dist > prev_jump+1:
                    break
            #print(nbors)
            return nbors
        
        def dfs(curr_stone,prev_jump):
            if curr_stone == len(stones) - 1: #Don't forget the -1
                return True #Curr stone must be the last stone
            elif (curr_stone,prev_jump) in memo:
                return False
            else:
                for nbor in get_nbors(curr_stone,prev_jump):
                    if dfs(nbor,stones[nbor]-stones[curr_stone]):
                        return True
                    memo.add((nbor,stones[nbor]-stones[curr_stone]))
                return False
            
        return dfs(0,0) #First jump must be 1 unit, frog starts on first stone @ pos=0