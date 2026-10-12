class Solution:
    def solve(self, board: List[List[str]]) -> None:

        #same as pacific atlantic problem
        # can solve this in a similar way to pacific atlantic problem. I can start from thhe   'O' cells at the edge, do a dfs from each cell to explore connected 'O', cells. Then, I can exceludee all these cells and replace all other 'O' cells that are not exclided with an 'X'.

        ROWS = len(board)
        COLS = len(board[0])

        #i exclude the 'O' cells connected to other 'O' cells that are adjacent to an edge

        def dfs(i, j):

            #end case, I get to an X, or to an already visited excluded cell, E
            if board[i][j] != 'O': return

            #nor for sure the O cell is connected to the edge by means of other O cells
            board[i][j] = 'E' #excluded from conquering

            for ni, nj in ((1,0), (0, 1), (-1, 0), (0,-1)):
                newi, newj = i+ni,j+nj
                if newi < 0 or newi >= ROWS or newj < 0 or newj >= COLS:
                    continue
                dfs(newi, newj)

        #exclude all regions connected to the edges
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS-1)
        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS-1, j)
        
        #now the remaining 'O' cells are landlocked and can be conquered
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O': board[i][j] = 'X'

        #restore excluded O cells
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'E': board[i][j] = 'O'
        