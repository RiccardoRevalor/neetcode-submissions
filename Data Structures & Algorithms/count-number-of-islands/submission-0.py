class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(i,j,grid):
            #i start dfs once i reach a 1
            #then i discover all connected 1s
            #and turn them into 0s

            #1 end
            if i == ROWS or j == COLS or i < 0 or j < 0: return

            #visit current cell, stopping when i find water
            if grid[i][j] == '0': return
            grid[i][j] = '0'
            #do recursion in neighbors
            dfs(i+1, j, grid)
            dfs(i, j+1, grid)
            dfs(i-1, j, grid)
            dfs(i, j-1, grid)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j, grid)
        return islands

        