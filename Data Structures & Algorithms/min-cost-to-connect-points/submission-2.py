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
        par1, par2 = self.find(n1), self.find(n2)
        if par1 == par2:
            return False
        
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
        elif self.rank[par1] < self.rank[par2]:
            self.par[par1] = par2
        else:
            self.par[par1] = par2
            self.rank[par2] += 1
        return True



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                manhattan = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, [manhattan, i, j])
        
        unionFind = UnionFind(len(points))
        mst = 0
        edges = 0

        while minHeap:
            distance, src, dst = heapq.heappop(minHeap)

            if not unionFind.union(src, dst) :  
                continue
            mst += distance
            edges += 1
        return mst if edges == (len(points) - 1) else -1

        
        