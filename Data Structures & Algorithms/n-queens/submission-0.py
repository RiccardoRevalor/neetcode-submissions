class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: return []
        board = [[0] * n for _ in range(n)]
        res = []

        def checkCell(board, row, col):
            #1: fix col, iterate on rows
            for i in range(n):
                if board[i][col]: return False
            #2:fix row, iterate over cols
            for j in range(n):
                if board[row][j]: return False

            #everything to theb RIGHT of the cell is for sure empty
            #so i just need to chedck the up left diagonal, and the bottom right diagonal
            #3:check left diagonal
            i, j1 = row, col
            while i >= 0 and j1 >= 0:
                #go up diagonally on left and check
                if board[i][j1]: return False
                #decrease rows, we climb up
                i-=1
                #left part, decrease cols
                j1-=1
            
            #same but on bottom right diagonal
            i, j1 = row, col
            while i < n and j1 >= 0:
                #go up diagonally on left and check
                if board[i][j1]: return False
                #increase rows, we climb up
                i+=1
                #right part, decrease cols
                j1-=1
            return True
            
                
        def matrixToStr(board):
            #retrun the format of the question
            res = []
            for i in range(n):
                colStr = ""
                for j in range(n):
                    if board[i][j]:
                        colStr += 'Q'
                    else: colStr += '.'
                res.append(colStr)
            return res


        
        def recur(board, col):
            #board id the temporary board i am constructing
            #col if the current col index

            #good ending: col == n, it means I've placed all n queens
            if col == n:
                res.append(matrixToStr(board))
                return

            #now, for each col, we try to put a queen in each row that passes the checks
            for row in range(n):
                if checkCell(board, row, col):
                    board[row][col] = 1 #place queen and recur
                    recur(board, col+1)
                    #remove placing
                    board[row][col] = 0
                #else skip cell
        
        recur(board, 0)
        return res

            
        