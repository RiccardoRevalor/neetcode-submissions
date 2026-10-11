class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()

        freshcounter = 0

        #1: put already rotten fruits in queue
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2: queue.append((i, j))
                elif grid[i][j] == 1: freshcounter +=1 

        #i need to count minutes
        #every BFS wave is a minute

        #do multi source bfs
        time = 0
        while queue and freshcounter > 0:
            #i split the waves to get a sense of time
            n = len(queue)
            for wave in range(n):
                i_rotten, j_rotten = queue.popleft()
                #look for fresh fruits to turn into rotten fruits
                for ni, nj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    fresh_i = i_rotten + ni
                    fresh_j = j_rotten + nj
                    #all checks
                    if fresh_i < 0 or fresh_i >= ROWS or fresh_j < 0 or fresh_j >= COLS: continue
                    if grid[fresh_i][fresh_j] == 1:
                        #fresh fruit found
                        grid[fresh_i][fresh_j] = 2
                        #put that in queue
                        queue.append((fresh_i, fresh_j))
                        freshcounter -= 1
            time += 1#after a wave, a min passes

        if freshcounter > 0: return -1
        return time
        
            

        
                

        