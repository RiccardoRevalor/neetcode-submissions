class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append([val, None]) #2nd term is the index of the element in min stack
        if len(self.mins) == 0:
            self.mins = [val]
            self.stack[-1][-1] = 0
            return

        if val <= self.mins[0]:
            self.mins = [val] + self.mins
            self.stack[-1][-1] = 0 
        else:
            self.mins = self.mins + [val]
            self.stack[-1][-1] = len(self.mins) - 1 #len is O(1) IN PYTHON!


        

    def pop(self) -> None:
        el = self.stack.pop()
        #delete from mins as well, here we need the index!
        self.mins.pop(el[1])
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.mins[0]
        
