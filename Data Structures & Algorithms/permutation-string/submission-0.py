class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Anagram == permutation?
        s1 = sorted(s1)
        s1 = "".join(s1) #Making s1 into a string to compare

        s2Freq = []
        for idx, val in enumerate(s2):
            s2Freq.append(val)
            if len(s2Freq) == len(s1): #It's a valid window
                s3 = sorted(s2Freq)
                s3 = "".join(s3)
                if s3 == s1:
                    return True
                #Start popping the left most char
                s2Freq.pop(0)
        return False