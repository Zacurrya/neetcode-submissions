class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            # Out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # Mark as visited
            grid[r][c] = 0

            area = 1
            dirs = [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]
            for r, c in dirs: area += dfs(r, c)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea

