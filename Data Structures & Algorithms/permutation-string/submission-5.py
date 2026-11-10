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

        for r in range(len(s2)):
            s2f[ord(s2[r]) - ord('a')] += 1
            
            if (r - l + 1) > len(s1):
                s2f[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if (r - l + 1) == len(s1):
                # Check if it exist or not 
                if tuple(s1f) == tuple(s2f):
                    return True
        
        return False 
            