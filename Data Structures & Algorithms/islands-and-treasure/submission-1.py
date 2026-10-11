class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #solution wiht multi-source BFS
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()

        #add all chests into queue
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0: queue.append((i,j))

        #now each time I pop from queue, I execute a wave of the bfs, so i update all distances of all adjacent cells at once

        
        while queue:
            #pop cell and update the distance of all neighbors
            #at beginning i pop the treasure
            i, j = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]: #all moves
                #check boundaries, and the cell must be not already visited (inf) etc
                neigh_i, neigh_j = i+di, j+dj
                if neigh_i >= 0 and neigh_i < ROWS and neigh_j >= 0 and neigh_j < COLS:
                    if grid[neigh_i][neigh_j] == 2147483647:
                        #visit cell and mark new distance, it is guaranteed it is the minimum because it is BFS
                        grid[neigh_i][neigh_j] = grid[i][j] +1
                        #push into queue
                        queue.append((neigh_i, neigh_j))


