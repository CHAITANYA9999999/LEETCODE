class Solution(object):
    def findItinerary(self, tickets):
        def dfs(node):
            if len(result) == len(tickets) + 1:
                return True

            if node not in graph:
                return False

            for i, neighbor in enumerate(graph[node]):
                if not visited[node][i]:
                    visited[node][i] = True
                    result.append(neighbor)
                    if dfs(neighbor):
                        return True
                    visited[node][i] = False
                    result.pop()

            return False

        graph = {}
        visited = {}

        for from_node, to_node in tickets:
            if from_node not in graph:
                graph[from_node] = []
                visited[from_node] = []

            graph[from_node].append(to_node)
            visited[from_node].append(False)

        for node in graph:
            graph[node].sort()

        result = ["JFK"]
        dfs("JFK")
        return result
