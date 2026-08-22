class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : 
            return ""
        sCount, tCount = {} , {}
        #Finding char frequencies on t
        for i in t :
            tCount[i] = 1 + tCount.get(i, 0)

        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(tCount) 
        # Why tCount ? Cause if we have 'aab' : ( a : 2, b : 1)
        # if we take len(t) we need have =3 which should not correct
        #it should only = 2 since when a = 2 -> have + 1, b = 1 -> have + 1
        l = 0
        for r in range(len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            #Since we not sure our tCount have s[r] in order to compare -> error
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]] :
                have += 1

            while have == need:
                #Updating our result
                if resLen > (r - l + 1):
                    res = [l , r]
                    resLen = r - l + 1
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] 
        #in case result not exist

            
          
            