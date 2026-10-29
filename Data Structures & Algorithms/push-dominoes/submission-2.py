class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #queue to simulate each second...every time we pop all L/R from queue, qwe update the array abd 1 second of simulation passes
        res = [d for d in dominoes]
        queue = deque()

        #first add all L/R into queue
        for i in range(len(dominoes)):
            d = dominoes[i]
            if d == '.': continue
            queue.append((d, i)) #L/R, index

        skippable = False #true when there is a R.L situation
        #i iterate through queue from left to right so when I pop a R I have to check we are not in R.L situation,, if we are set skippable to True and when we pop next L we skip it
        while queue:
            falling = queue.popleft()
            if skippable:
                skippable = False
                continue
            
            #if L, if index -1 is a ., make it L
            falling_index = falling[1]
            falling_type = falling[0]

            if falling_type == 'L':
                if falling_index -1 >= 0 and res[falling_index-1] == '.':
                    #update res + add new L to queue, at the end
                    res[falling_index-1] = 'L'
                    queue.append(('L', falling_index-1))
                    continue

            if falling_type == 'R':
                #first check that falling_index+2 is not L
                if falling_index +2 < len(res):
                    if res[falling_index +2] == 'L' and res[falling_index + 1] == '.':
                        #we are in R.L situation, skip next L
                        #do not update res
                        skippable = True
                        continue
                
                #if not, set item at falling_index+1 equal to R
                if falling_index +1 < len(res) and res[falling_index+1] == '.':
                    res[falling_index+1] = 'R'
                    queue.append(('R', falling_index+1))

        #at the end queue is empty, aka simulation finished
        return "".join(res)




