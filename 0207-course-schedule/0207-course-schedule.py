class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        self.memo={}
        for course,prerequisite in prerequisites:
            if course not in self.graph:
                self.graph[course] = set()
            self.graph[course].add(prerequisite)
        for i in range(numCourses):
            print(i)
            if not self.checkIfCanFinish(i,[False]*numCourses):
                return False
            print("abracadabra")
        return True
    
    def checkIfCanFinish(self,node,visited):
        if node not in self.graph:
            self.memo[node] = True
            return True
        if node in self.memo:
            return self.memo[node]
        if visited[node]:
            return False
        visited[node] = True
        for prerequisites in self.graph[node]:
            if not self.checkIfCanFinish(prerequisites,visited):
                self.memo[node] = False
                return False
        self.memo[node] = True
        return True