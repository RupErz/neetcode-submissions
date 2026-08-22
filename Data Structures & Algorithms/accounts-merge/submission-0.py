class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, x, y):
        pX, pY = self.find(x), self.find(y)
        if pX == pY:
            return False
        
        if self.rank[pX] > self.rank[pY]:
            self.par[pY] = pX
        elif self.rank[pX] < self.rank[pY]:
            self.par[pX] = pY
        else:
            self.par[pX] = pY
            self.rank[pY] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        # So we can insta know when it overlap or not
        emailToIndex = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                # If we already have this email marked
                if e in emailToIndex:
                    uf.union(i, emailToIndex[e])
                else :
                    emailToIndex[e] = i
        
        # Generating a dictionary with each default value is a list
        # index : [ emails ]
        groupEmail = defaultdict(list)
        for e, i in emailToIndex.items():
            # Since we alr merge, some index might be child of another index
            leaderIndex = uf.find(i) 
            groupEmail[leaderIndex].append(e)
        
        result = []
        for i, emails in groupEmail.items():
            name = accounts[i][0]
            # In python we can do list concatenation
            result.append([name] + sorted(emails))
        
        return result 

        