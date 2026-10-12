class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #I can create the graph by putting one edge at a time
        #before inserting it, i first check if graph is already fully connected, i.e. if i can already reach node1 from node0. If i can, it means that the edge is redundant and I can remove it

        G = defaultdict(list)

        def connected(currNode, target, visited):
            #good case, i can reach target
            if currNode == target: return True

            visited.add(currNode)
            for neigh in G[currNode]:
                if not neigh in visited:
                    if connected(neigh, target, visited): return True  #i found a path from src to target
            
            #not connected
            return False

        #build the graph by inserting one adge at the time
        #before inserting the edge, check if I can already reach the two nodes in the edge I wanna insert. If I can, it means that the edge is redundat
        
        for source, target in edges:
            redundant = connected(source, target, set())
            if redundant: return [source, target]
            #add the edge to the chart
            G[source].append(target)
            G[target].append(source)

        return []

        