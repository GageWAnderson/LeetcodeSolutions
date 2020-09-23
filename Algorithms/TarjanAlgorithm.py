#Tarjan's algorithm is used to find Articulation points in a graph
#Can be used to get critical connections in a network
#Non-trivial, just memorize the outline for this code

#This is DFS with 3 additional arguments for bookeeping
class TarjanAlgorithm:
    def __init__(self):
        self.visited = set()
        self.artPoints = set()
        self.visitedTime = dict()
        self.lowTimes = dict()
        self.parents = dict()
        self.time = 0

    def tarjanDFS(self,G,start):
        self.visited.add(start)
        self.visitedTime[start] = self.time
        self.lowTimes[start] = self.time
        self.time += 1

        childCount = 0
        isArtPoint = False
        for nbor in G.getNbors(start):
            if nbor==start:
                #Ignore duplicates
                continue
            if nbor not in self.visited:
                self.parents[nbor] = start
                childCount += 1
                self.tarjanDFS(G,nbor) #Recurse here

                if self.visitedTime[start] <= self.lowTimes[nbor]:
                    isArtPoint = True
                else:
                    self.lowTimes[start] = min(self.lowTimes[start],self.lowTimes[nbor])
            else:
                self.lowTimes[start] = min(self.lowTimes[start],self.lowTimes[nbor])

        if not self.parents[start] and childCount >= 2:
            self.artPoints.add(start)
        elif self.parents[start] and isArtPoint:
            self.artPoints.add(start)