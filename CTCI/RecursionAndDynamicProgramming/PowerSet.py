from copy import deepcopy

class PowerSet:
    
    def __init__(self, values):
        self.values = values

    # Top-down recursion approach
    # No DP necessary, since the problem statement is to FIND ALL subsets
    def powerSet(self): # Returns all subsets of a set
        ans = []
        seen = set()

        def helper(subset):
            print(f"subset = {subset}")
            if len(subset) == 1:
                if tuple(subset) not in seen:
                    seen.add(tuple(subset))
                    ans.append(deepcopy(subset))
            else:
                for i,elem in enumerate(subset):
                    subset.pop(i)
                    if tuple(subset) not in seen:
                        seen.add(tuple(subset))
                        ans.append(deepcopy(subset))
                        helper(subset)
                    subset.append(elem)
                    subset[-1],subset[i] = subset[i],subset[-1]
        
        helper(self.values)
        ans.append([]) # All subsets includes the empty set
        return ans

if __name__ == "__main__":
    testSet = PowerSet([1, 2, 3, 4, 5, 6])
    print(testSet.powerSet())