from collections import deque
class BFS:
    def bfs(self,graph,start):
        q = deque()
        q.append(start)
        seen = set()

        while q:
            node = q.popleft()
            print(node)

            if node not in seen:
                seen.add(node)
                nbors = self.getNbors(node,graph)
                for nbor in nbors:
                    q.append(nbor)