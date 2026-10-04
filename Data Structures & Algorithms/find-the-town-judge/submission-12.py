class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        scores = [0] * (n+1)

        for pair in trust:
            trusted = pair[1]
            truster = pair[0]
            scores[trusted] += 1
            scores[truster] -=1 #penalty because judge trusts nobody

        for person in range(n+1):
            if scores[person] == n-1: return person


        
        return -1
        