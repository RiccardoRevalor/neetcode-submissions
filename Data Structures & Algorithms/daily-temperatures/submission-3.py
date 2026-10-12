class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        min = float('inf')

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            t = temperatures[i]

            if t <= min: 
                #push into stack
                stack.append((i, t)) #index, t
                #update min
                min = t

            else:
                while stack:
                    #pop each element and compute diff in days as long as the element is less
                    el_i, el_t = stack.pop()
                    if el_t >= t: 
                        stack.append((el_i, el_t))
                        break
                    #difference in days is i - el_i, for the element at el_i
                    res[el_i] = i - el_i
                
                stack.append((i, t))
                min = t

        return res





        