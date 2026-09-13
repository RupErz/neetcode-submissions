class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        # Each node is a parent of itself
        # Merge: the lower with the bigger one + update its size
        # adj = {i:[] for i in range(n)}
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        

        # visited = set()
        # def dfs(cur):
        #     if cur in visited:
        #         return
            
        #     visited.add(cur)
        #     for nei in adj[cur]:
        #         dfs(nei)


        # result = 0
        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         result += 1
        
        # return result

        # Union Find
        par = [i for i in range(n)]
        rank = [1] * n

        # each node is parent of itself + its rank (# nodes) = 1
        def find(n):
            res = n
            while res != par[res]:
                par[res]= par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if p1 >= p2:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1 # We just merge 2 into 1 pairs
        
        result = n
        # Everytime we merge 2 we -1 in total nodes
        for u, v in edges:
            result -= union(u, v)
        return result
