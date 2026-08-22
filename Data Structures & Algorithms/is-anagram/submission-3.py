class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a dict to count the freq of each char
        freq = {}

        for cs in s:
            if cs not in freq:
                freq[cs] = 0
            freq[cs] += 1
        # compare it against the newest one 

        # if there still exist value in freq1 -> False

        for ct in t:
            if ct not in freq:
                return False
            
            if freq[ct] - 1 == 0:
                del freq[ct]
            else:
                freq[ct] -= 1
        
        
        return True if not freq else False