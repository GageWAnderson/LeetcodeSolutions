# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
  
# Library for INT_MAX 
import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print "Vertex \tDistance from Source"
        for node in range(self.V): 
            print node, "\t", dist[node] 
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxint 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  
        dist = [sys.maxint] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex is not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and \ 
                dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 
  

#Algorithm Pseudocode:
"""
Let distance of start vertex from start vertex = 0
Set all other distances to sys.maxint

Repeat:
    Visit the unvisited vertex with the smallest known distance from the start O(V)
    For the current vertex, examine its unvisited neighbours

    For the current vertex, calculate distance of each nbor from the start vertex
    If the calculated distance of a vertex is less than the known distance, update the shortest distance
    Update the previous vertex for each of the updated distances
    Add the current vertex to the set of visited verticies
Until All visited
"""

class MyDijkstras:
    def minDist(self,dists):
        min_index = -1
        min_so_far = sys.maxint
        for i in range(len(dists)):
            if dists[i] < min_so_far:
                min_so_far = dists[i]
                min_index = i
        return min_index
        
    def Dijkstra(self,Graph,start,target): #Works for Adjacency matrix Graph implementation
        unvisited = [v for v in Graph]
        distances = [sys.maxint for v in Graph]
        distances[start] = 0
        visited = [False for v in Graph]

        for v in Graph: #O(V), need to look at all verticies
            u = self.minDist(distances) #O(V), linear search
            if u == target:
                return distances[u]
            visited[u] = True

            for v in Graph:
                if Graph[u][v] > 0 and visited[v] == False and distances[v] > distances[u] + Graph[u][v]:
                    distances[v] = distances[u] + Graph[u][v]
        return distances[target]
