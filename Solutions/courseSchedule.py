from collections import defaultdict

class SolutionDFS(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False # Cycle detected, return false
            if graph[course] == []:
                return True # Base case, return true since found no cycles
            
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            graph[course] = [] # Visited these courses, don't need to consider again
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True