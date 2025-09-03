class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # recursive dfs
        m, n = len(grid), len(grid[0])
        count = 0
        
        # the number of recursive dfs calls == the number of islands
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":  # base case
                return

            # "sink" any visited land to mark as visited
            grid[i][j] = 0

            # propagate in all four directions
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        # recursively call dfs everytime an unvisited land is encountered
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count


