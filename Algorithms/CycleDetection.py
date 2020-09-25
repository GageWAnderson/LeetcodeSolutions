class DetectCycle: #O(V) Time and space complexity

    #All you need to do is visit a non-parent vertex that is
    #Already in seen
    def detectCycleUndirected(self,graph):
        seen = {v:False for v in graph}

        def _dfs(start,parent):
            seen[start] = True
            for nbor in graph[start]:
                if not parent or (nbor != parent and seen[nbor] == False):
                    if dfs(nbor,start):
                        return True
                elif nbor != parent and nbor in seen:
                    return True
            return False

        return _dfs(graph[0],None)

    #For connected components, detect cycles by finding back-edges.
    def detectCycleDirected(self,graph):
        seen = {v:False for v in graph}
        rec_stack = {v:False for v in graph}

        def isCyclic(n):
            seen[n] = True
            rec_stack[n] = True

            #Recur for all nbors of n, if any are in visited
            #And also in rec_stack then the graph has a cycle
            for nbor in graph[n]:
                if not seen[nbor]:
                    if isCyclic(nbor):
                        return True
                    elif rec_stack[nbor]:
                        return True

            #The node needs to be popped from rec_stack
            rec_stack[n] = False
            return False

        for node in graph:
            if seen[node] == False:
                if isCyclic(node):
                    return True
        return False

