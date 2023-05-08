"""
This problem was too hard. I got the approach but had no idea
where to start on the implementation. Broke me out of my flow-state
due to being far in excess of the '+4%' difficulty rule.
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str: 
        graph = { c : set() for word in words for c in word }

        # Construct the lexicographic graph word by word by comparing them
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        visit = {}
        res = []

        # Topological Sort is DFS in reverse (just return reversed(stack)) of results
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nbor in graph[c]:
                if dfs(nbor):
                    # Cycle detected, not a valid DAG
                    return True
            visit[c] = False
            res.append(c)

        for c in graph:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)