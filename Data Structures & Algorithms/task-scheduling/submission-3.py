class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #here it is better to first schedule tasks that are repeated, and spread them around in the sheduling, so I can use a max heap to count frequencies of each task (task going from 0 to 26) and at each time pop the task having max freq
        freqs = {}
        for t in tasks:
            if t in freqs: freqs[t]+=1
            else: freqs[t] = 1

        #caveat: python just has min heaps, so invert freqs
        heap = [(-f, t) for t, f in freqs.items()] #(-f, t)
        heapq.heapify(heap) 

        #fifo queue for cooldown
        #at each cycle, i pop a task from the heap
        #popped task DO NOT GO into heap anymore, they go into cooldown
        #so I'll get to a certain point in which heap is empty buit we still have the cooldown
        cycles = 0
        cooldown = deque() #(f, t, next steps in which I an execute it)
        while len(heap) > 0 or len(cooldown) > 0:
            cycles += 1
            #pop the most freq task which is not in the cooldown period

            if heap:
                #we CAN EXECUTE A TASK
                #always exec a task with highest freq first
                (f, t) = heapq.heappop(heap)
                #print(t)
                #decrement frequency
                #or actually increment since we are using a min heap
                f +=1
                #if the task still has freq < 0, put it in queue
                if f < 0:
                    cooldown.append((f, t, cycles + n))
                    #this way, in queue i'm first gonna put the most frequent tasks, because they are extracted first from the heap
            #else: print("I") #idle
            
            #if idle has gone ans we can execute from queue:
            if cooldown and cooldown[0][2] == cycles:
                #reinsert into heap to execite again
                f, t, _ = cooldown.popleft()
                heapq.heappush(heap, (f, t))

        return cycles

            






        
            
        

        