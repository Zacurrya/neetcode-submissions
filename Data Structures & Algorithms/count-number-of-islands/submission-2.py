class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numOfIslands = 0

        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "0"

            # Dfs on adjacent nodes
            dirs = [[r+1,c], [r-1,c], [r,c+1],[r,c-1]]
            for r, c in dirs:
                if (r >= 0) and (r < rows) and (c >= 0) and (c < cols) and grid[r][c] == "1": 
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                # New island found
                if grid[r][c] == "1":
                    dfs(r, c)
                    numOfIslands += 1
    


        return numOfIslands