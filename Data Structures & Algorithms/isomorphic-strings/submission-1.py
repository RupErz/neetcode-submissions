class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mappingS = {}
        mappingT = {}

        for i in range(len(s)):
            curS, curT = s[i], t[i]
            if (curS in mappingS and mappingS[curS] != curT) or (curT in mappingT and mappingT[curT] != curS):
                return False
            
            mappingS[curS] = curT
            mappingT[curT] = curS
        
        return True
        