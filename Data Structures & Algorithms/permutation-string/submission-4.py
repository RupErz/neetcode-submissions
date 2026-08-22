class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # Anagram == permutation?
        # #Sol1 : Time(O(NlogN))
        # s1 = sorted(s1)
        # s1 = "".join(s1) #Making s1 into a string to compare

        # s2Freq = []
        # for idx, val in enumerate(s2):
        #     s2Freq.append(val)
        #     if len(s2Freq) == len(s1): #It's a valid window
        #         s3 = sorted(s2Freq)
        #         s3 = "".join(s3)
        #         if s3 == s1:
        #             return True
        #         #Start popping the left most char
        #         s2Freq.pop(0)
        # return False

        #Using Array not Hashmap
        if len(s1) > len(s2) : return False

        s1Count, s2Count = [0] * 26, [0] * 26 #26 alpha char
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ ord(s2[i]) - ord('a')] += 1
        #Recording the frequencies of each char

        matches = 0 #Keep track of how many matches char we have , if 26:T
        #Update our matches with 2 array count
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        #start at the next char since we alr check first 3 of s2
        for r in range(len(s1), len(s2)):
            if matches == 26 : return True

            #Checking after add
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] - 1 == s1Count[index]:
                matches -= 1

            #Checking after pop
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] + 1 == s1Count[index]:
                matches -= 1
            
            l += 1
        return matches == 26
            


        
