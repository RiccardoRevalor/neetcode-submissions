class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) #key: index of row r
        cols = defaultdict(set) #key: index of col c
        boxes = defaultdict(set) #key: index of box = (r // 3) * 3 + col // 3

        ROWS = len(board)
        COLS = len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                b = board[r][c]

                #skip empty cell
                if b == '.': continue

                #if b value is already in either 1 or more of the sets, return False
                if b in rows[r]: return False
                if b in cols[c]: return False
                boxindex = (r // 3) * 3 + (c // 3)

                if b in boxes[boxindex]: return False

                #update sets
                rows[r].add(b)
                cols[c].add(b)
                boxes[boxindex].add(b)

        return True

        