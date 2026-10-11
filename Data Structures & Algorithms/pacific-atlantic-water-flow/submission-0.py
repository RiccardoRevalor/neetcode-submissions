class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        atlanticSet = set()
        pacificSet = set()

        #we star by selecting all cells bordering atlantic and pacific and put them in the sets
        #pacific, all 1 row, all 2 col
        #atlantic, add last row, all last col

        #if i do a DFS/BFS starting form each cell, it sould take O(m*n)^2

        #so instead i can do a DFS of from each ocean, to find all cels that reach that specific oceean
        #then i can take the intersection of the two sets

        def recur(i,j,thresh, visited):
            #end condition
            #out of boundaries
            #current value of the cell is < thresh
            #if i < 0 or i >= ROWS or j < 0 or j >= COLS: return

            if heights[i][j] < thresh: return

            #add to set ans visit cell
            visited.add((i,j))
            for ni, nj in ((1,0), (0,1), (-1, 0), (0,-1)):
                newi, newj = i+ni, j+nj
                if newi < 0 or newi >= ROWS or newj < 0 or newj >= COLS: continue
                #prune cells already visited, not need to vist them again
                if not (newi, newj) in visited: recur(newi, newj, heights[i][j], visited)

        #do DFS for both oceans

        for j in range(COLS):
            recur(0, j, 0, pacificSet)
            recur(ROWS-1,j,0, atlanticSet)
        for i in range(ROWS):
            recur(i, 0, 0, pacificSet)
            recur(i, COLS-1, 0, atlanticSet)
        #solution is intersection of two sets
        sol = pacificSet & atlanticSet
        return [cell for cell in sol]







            


        

        