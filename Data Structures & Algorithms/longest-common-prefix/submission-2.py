class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            curLetter = strs[0][i]
            for j in strs[1:]:
                if i not in range(len(j)) or curLetter != j[i]:
                    return result
        
            result += curLetter
        
        return result