class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t == "" : 
        #     return ""
        # sCount, tCount = {} , {}
        # #Finding char frequencies on t
        # for i in t :
        #     tCount[i] = 1 + tCount.get(i, 0)

        # res, resLen = [-1, -1], float("infinity")
        # have, need = 0, len(tCount)
        # l = 0
        # for r in range(len(s)):
        #     sCount[s[r]] = 1 + sCount.get(s[r], 0)
        #     #Since we not sure our tCount have s[r] in order to compare -> error
        #     if s[r] in tCount and sCount[s[r]] == tCount[s[r]] :
        #         have += 1

        #     while have == need :
        #         #Updating our result
        #         if resLen > (r - l + 1):
        #             res = [l , r]
        #             resLen = r - l + 1
        #         sCount[s[l]] -= 1
        #         if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
        #             have -= 1
        #         l += 1
        #     l, r = res
        # return s[l : r + 1] if resLen != float("infinity") else ""
        # #in case result not exist
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            
          
            