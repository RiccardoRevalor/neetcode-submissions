class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #a tree has no cyces and is connected, i.e. there are no nodes that are alone

        #it has to have n-1 edges 
        if len(edges) != n-1: return False

        visited = set() #sine this is undiretced, I can just use the visited set, instead of the double check of directed graphs

        #create a hashmap from the list
        G = defaultdict(list)
        #key: node, value: list of neighbors
        for node1, node2 in edges:
            G[node1].append(node2)
            G[node2].append(node1)

        def dfs(node):
            #just visit nodes, since thye are undirected, edge detection is not needed

            visited.add(node)

            for neigh in G[node]:
                if neigh not in visited: dfs(neigh)
        

        #if i visited every node, it means that i do not have separate nodes
        dfs(0)
        return len(visited) == n
                

        
        