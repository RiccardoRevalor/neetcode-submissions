class Solution:
    def isValid(self, s: str) -> bool:
        #for sure if len is odd, return False
        n = len(s)
        if n % 2 != 0: return False

        stack = [] #for last opened pars

        open0, open1, open2 = 0, 0, 0 
        

        for ch in s:
            if ch == '(': 
                open0 +=1
                stack.append(ch)
            if ch == '[': 
                open1 +=1
                stack.append(ch)
            if ch == '{': 
                open2 +=1
                stack.append(ch)

            #troubles happens when closing
            if ch == ']':
                if open1 == 0: return False 
                open1 -=1
                if stack[-1] != '[': return False
                stack.pop()
            if ch == ')':
                if open0 == 0: return False 
                open0 -=1
                if stack[-1] != '(': return False
                stack.pop()
            if ch == '}':
                if open2 == 0: return False 
                open2 -=1
                if stack[-1] != '{': return False
                stack.pop()

        return open0 == 0 and open1 == open0 and open2 == open0
            

        