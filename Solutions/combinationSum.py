from collections import Counter

"""
This is a 'find all' problem, so backtracking is the only solution.

I ended up trying too hard with constant-time lookup structures (frozenset), when a
list would suffice -
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        seen = set()
        targetSumSet = set()

        def helper(numsBag, currSum, currIndex):
            currNumsBag = frozenset(numsBag.items())
            # if currNumsBag in seen: # Memoization
            #     return
            
            seen.add(currNumsBag)
            if currSum == target:
                if currNumsBag not in targetSumSet:
                    print(f"currNumsBag = {currNumsBag}, targetSumSet = {targetSumSet}")
                    targetSumSet.add(currNumsBag)
                return
            elif currSum > target:
                return
            else:
                for num in candidates[currIndex:]:
                    # The num is either in or out of the set, can be used twice
                    numsBag.update([num])
                    helper(numsBag, currSum + num, currIndex + 1)
                    helper(numsBag, currSum + num, currIndex) # Keep using the current num
                    # Not an infinite loop due to every number being positive
                    numsBag.subtract([num])
                    if numsBag[num] == 0:
                        del numsBag[num] # Remove elements from the counter if they reach 0
                    helper(numsBag, currSum, currIndex + 1)
                return
        
        helper(Counter(), 0, 0)
        res = []
        for counter in targetSumSet:
            counterList = list(counter)
            thisBag = []
            for freq in counterList:
                if freq[1] > 0:
                    for i in range(freq[1]):
                        thisBag.append(freq[0])
            res.append(thisBag)
        return res


"""
Optimal solution prevents duplicates in the result by recognizing that all the
combinations traversed by the backtracking tree are unique. Therefore, there is
no need to track them to prevent duplicates, and they can be directly added to the set.
"""
class SolutionOptimal:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return # Found a solution
            elif i >= len(candidates) or total > target:
                return # Can't find a solution here
            else:
                # Try including a copy of current num in res or move on (2 options in decision tree)
                cur.append(candidates[i])
                dfs(i, cur, total + candidates[i])
                cur.pop()
                dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res