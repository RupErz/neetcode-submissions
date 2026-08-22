class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        parN1, parN2 = self.find(n1), self.find(n2)
        
        # Avoid Cycle
        if parN1 == parN2 :
            return False
        
        if self.rank[parN1] > self.rank[parN2]:
            self.par[parN2] = parN1
        elif self.rank[parN1] < self.rank[parN2]:
            self.par[parN1] = parN2
        else:
            self.par[parN1] = parN2
            self.rank[parN2] += 1

        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        unionFind = UnionFind(n)

        for src, dst, w in edges:
            heapq.heappush(minHeap, [w, src, dst])

        mst = 0
        edges = 0
        while minHeap:
            w, src, dst = heapq.heappop(minHeap)

            # If we cant merge -> Cycle probably
            if not unionFind.union(src, dst):   
                continue
            
            mst += w
            edges += 1
        return mst if edges == n - 1 else -1
