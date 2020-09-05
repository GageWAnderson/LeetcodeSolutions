#All possible sentences -> implies backtracking with DFS
#Use DP to bring down the time for the solution ? -> seems like this isn't possible
#Since we need to return all possible sentences
class SolutionSlow:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        limit = len(s)
        res = []
        #Need memoization or I'm going to get TLE due to exponential time
        def dfs(s,curr,index):
            #print(curr)
            if s in wordSet: #Shouldn't append to curr here, otherwise I was right
                res.append(" ".join(curr + [s]).strip())
            if index == limit:
                return
            for i in range(len(s)):
                if s[:i+1] in wordSet:
                    curr.append(s[:i+1])
                    dfs(s[i+1:],curr,i+1)
                    curr.pop()
        
        dfs(s,[],0)
        return res
        

class SolutionMemoized:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        memo = {}
        
        def dfs(s):
            # Returns a list of list if valid, else returns an empty list
            if not s:
                # Empty string is a valid result
                return [[]] 
				
            if s in memo:
                # Seen already
                return memo[s]
            
            memo[s] = []
            
            for word in wordDict:
                if s.startswith(word):
                    result_of_rest = dfs(s[len(word):])
                    
                    if not result_of_rest:
                        # If the result of rest of the string is invalid, just continue
                        continue
                    
                    # Left append the current word to all the lists of result_of_rest
                    memo[s] += list(map(lambda x: [word] + x, result_of_rest))
                    
            return memo[s]
        
        dfs(s)
        return list(map(lambda x: " ".join(x), memo[s]))