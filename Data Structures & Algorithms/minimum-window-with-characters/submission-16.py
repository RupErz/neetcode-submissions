class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window
        # Keep sliding until found a valid window
            # Shrinking left until non valid
        # Repeat

        # How to check if t is in a substring / curWindow 
        
        # Count how many char in t
        Tfreq = {}
        for c in t:
            if c not in Tfreq:
                Tfreq[c] = 0
            Tfreq[c] += 1
        
        # window hash to track validity
        curWindow = {}
        need = len(Tfreq) #. distince char of t
        have = 0 # only update if curWindow satisfy total amount of a ch

        l = 0
        result = ""
        for r in range(len(s)):
            curChar = s[r]
            
            if curChar not in curWindow:
                curWindow[curChar] = 0
            curWindow[curChar] += 1

            if curChar in Tfreq and curWindow[curChar] == Tfreq[curChar]:
                have += 1
            
            # Shrinking the window till invalid
            while have == need:
                if not result or (r - l + 1) < len(result):
                    result = s[l:r+1]

                curWindow[s[l]] -= 1
                if s[l] in Tfreq and curWindow[s[l]] < Tfreq[s[l]]:
                    have -= 1
                l += 1
                
        
        return result
            


            
