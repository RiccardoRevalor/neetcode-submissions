class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        #a/b = 4
        #b / c = 1
        #graph: a ->(4) b ->(1) c
        #i wanna know a /c
        #a/c = a / b * b / c = 4 * 1 = 4
        #if i wanna know c / a
        #c / a = 1 / 1 * 1 / 4 = 0.25
        #bfs to start from source and find dest

        G = defaultdict(list) #adj
        #key: every source, value: every connected neighbor + the source / neighbor value

        for index, eq in enumerate(equations):
            source, neigh = eq
            source_div_neigh = values[index]
            #add both source and neigh as source noides
            G[source].append([neigh, source_div_neigh])
            G[neigh].append([source, 1 / (source_div_neigh)])


        def bfs(source, dest):
            #bad case: one or two nodes not in G
            if not source in G: return -1
            if not dest in G: return -1

            q = deque() #node, current multiplication up to that node
            q.append([source, 1])
            visited = set()
            visited.add(source)
            
            while q:
                node, mult = q.popleft()
                #iterate through all neigh of node
                #if node == dest, return mult
                if node == dest: return mult
                #else: iterate through neighbors
                for neigh, source_div_neigh in G[node]:
                    #if not already visited
                    if neigh in visited: continue
                    visited.add(neigh)
                    q.append([neigh, mult * source_div_neigh]) #update running mult



            return -1 #if we do not have source /dest, but both source and dest are in G



        res = []
        for source, dest in queries:
            res.append(bfs(source, dest))

        return res
        