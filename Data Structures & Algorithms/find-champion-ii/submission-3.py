class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        #all the v edges in [u,v] are weaker than a u and we don't consider them
        vs = set(v for u,v in edges)
        candidates = set(u for u in range(n) if u not in vs) #we have to consider also the edges not in the graph but still existent -> There are n teams labeled 0 through n - 1
        if not candidates: return -1
        if len(candidates) > 1: return -1
        return list(candidates)[0]


        