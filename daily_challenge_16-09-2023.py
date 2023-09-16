class Solution:
    def __init__(self):
        self.visited = []  # Visited cells tracker
        self.directions_x = [0, 1, -1, 0]  # Changes in x coordinate for four directions
        self.directions_y = [1, 0, 0, -1]  # Changes in y coordinate for four directions
        self.numRows = 0
        self.numCols = 0

    # Depth-First Search to explore the path with a given maximum effort
    def dfs(self, x, y, limit_effort, heights) -> None:
        if self.visited[x][y]:
            return
        self.visited[x][y] = True

        # Stop if we've reached the bottom-right cell
        if x == self.numRows - 1 and y == self.numCols - 1:
            return

        # Explore each direction (up, down, left, right)
        for i in range(4):
            new_x = x + self.directions_x[i]
            new_y = y + self.directions_y[i]

            # Check if the new coordinates are within bounds
            if new_x < 0 or new_x >= self.numRows or new_y < 0 or new_y >= self.numCols:
                continue

            # Go to next cell if the effort is within maximum
            new_effort = abs(heights[x][y] - heights[new_x][new_y])
            if new_effort <= limit_effort:
                self.dfs(new_x, new_y, limit_effort, heights)

    def minimumEffortPath(self, heights) -> int:
        self.numRows = len(heights)
        self.numCols = len(heights[0])

        # Initialize visited array
        self.visited = [[False for _ in range(self.numCols)] for _ in range(self.numRows)]

        # Bound for our binary search
        lower_limit, upper_limit = 0, 1000000

        while lower_limit < upper_limit:
            mid = (upper_limit + lower_limit) // 2

            # Reset visited array
            self.visited = [[False for _ in range(self.numCols)] for _ in range(self.numRows)]

            self.dfs(0, 0, mid, heights)

            if self.visited[self.numRows - 1][self.numCols - 1]:
                upper_limit = mid
            else:
                lower_limit = mid + 1

        return lower_limit