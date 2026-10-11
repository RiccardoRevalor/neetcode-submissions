class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(i,j,grid):
            #i start dfs once i reach a 1
            #then i discover all connected 1s
            #and turn them into 0s

            #1 end
            if i == ROWS or j == COLS or i < 0 or j < 0: return 0

            #visit current cell, stopping when i find water
            if grid[i][j] == 0: return 0
            grid[i][j] = 0
            #do recursion in neighbors
            area = 1
            area += dfs(i+1, j, grid)
            area += dfs(i, j+1, grid)
            area += dfs(i-1, j, grid)
            area += dfs(i, j-1, grid)

            return area

        best = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = dfs(i, j, grid)
                    best = max(best, area)
        return best

        