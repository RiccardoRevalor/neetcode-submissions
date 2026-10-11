class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set() #for the already visited cells, not to visit them again

        def dfs(i, j, wordindex):
            #i = index of the current visited cell
            #j = index of the current visited cell
            #wordindex: index of the current letter of the word i'm trying to match
            #good ending: i fully match the word!
            if wordindex >= len(word): return True #END
            #GOOD ENDING NEEDS TO GO BEFORE 

            #bad endings: i go past the boundaries
            if i >= rows or j >= cols or i < 0 or j < 0: return False
            #and ending: the curremt cell breaks the word, i.e. i cannot mathc the letter
            #in this case i have to backtrack and he try another cell, adjacent to the previously matched cell
            if board[i][j] != word[wordindex]: return False #backtrack
            #if i already explored the cell, no sense in exploring it again
            if (i, j) in path: return False


            #explore current cell
            #if i arrived here, it means that word[wordindex] == board[i][j]
            #good, so advance the index and try adjacent cells to continue matching the word
            #add current cell to path
            path.add((i,j))

            #try to see if any of the 4 adjacent cells leads to a complete match
            newindex = wordindex+1
            res = dfs(i+1, j, newindex) or dfs(i,j+1,newindex) or dfs(i-1, j,newindex) or dfs(i,j-1,newindex)
            #free cell from path, so that otheer completely different paths can explore it
            path.remove((i,j))
            return res

        #do a complete dfs for each cell, i.e. i chose each cell as starting cell and do the dfs from there
        for i in range(rows):
            for j in range(cols):
                found = dfs(i,j,0)
                if found: return True

        return False
        