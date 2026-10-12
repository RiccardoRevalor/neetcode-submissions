class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for node1, node2 in edges:
            G[node1].append(node2)
            G[node2].append(node1)

        visited = set()
        
        def dfs(node):
            visited.add(node)

            for neigh in G[node]:
                if neigh not in visited: dfs(neigh)

        wave = 0
        while len(visited) < n:
            for i in range(n):
                if i in visited: continue
                dfs(i) #here in the same wave i visit a fully connected portion of the graph
                wave +=1

        return wave



        