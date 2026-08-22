class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution 1 : Create 2 hashmap , record ocurrences of character and 
        #then compare
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for n in countS : #Loop through a key
            if countS[n] != countT.get(n, 0): #countTmight dont have that although same length
                return False
        return True