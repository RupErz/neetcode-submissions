class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # How do u find something include in another thing
        # 2 ptrs , and start checking if saw keypoint 

        # How do u check Permutations ? 

        if len(s1) > len(s2):
            return False

        s1f = [0] * 26
        for l in s1:
            s1f[ord(l) - ord('a')] += 1
        
        s2f = [0] * 26
        l = 0

        matches = sum(1 for i in range(len(s1f)) if s1f[i] == s2f[i])

        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')

            if s1f[idx] == s2f[idx]:
                matches -= 1
            s2f[idx] += 1
            if s2f[idx] == s1f[idx]:
                matches += 1
      
            
            if (r - l + 1) > len(s1):
                idxL = ord(s2[l]) - ord('a')

                if s2f[idxL] == s1f[idxL]:
                    matches -= 1
                s2f[idxL] -= 1
                if s2f[idxL] == s1f[idxL]:
                    matches += 1

                l += 1
            
            if (r - l + 1) == len(s1):
                # Check if it exist or not 
                if matches == 26:
                    return True
        
        return False 
            