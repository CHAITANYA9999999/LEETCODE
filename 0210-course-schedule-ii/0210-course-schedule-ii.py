from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize the in-degree array and the adjacency list
        in_degree = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        
        # Build the graph
        for course, pre in prerequisites:
            in_degree[course] += 1
            adj_list[pre].append(course)
        
        # Queue for courses with no prerequisites (in-degree 0)
        available = [i for i in range(numCourses) if in_degree[i] == 0]
        
        res = []
        
        while available:
            course = available.pop(0)
            res.append(course)
            # Decrease the in-degree of the neighboring courses
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    available.append(neighbor)
        
        # If the result size is equal to numCourses, we found a valid order
        if len(res) == numCourses:
            return res
        else:
            # If we couldn't include all courses, there's a cycle
            return []
