class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            grid[r][c] = "0"
            
            dirs = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
            for dr, dc in dirs:
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                    dfs(dr, dc)


        numOfIslands = 0

        for r in range(rows):
            for c in range(cols):
                # run dfs on new island
                if grid[r][c] == "1":
                    numOfIslands += 1            
                    dfs(r, c)

        return numOfIslands
                
                    