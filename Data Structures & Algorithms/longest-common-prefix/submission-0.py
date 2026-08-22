class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            # Looping through each available strings
            for str in strs:
                if i not in range(len(str)) or str[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result


        # Psedocode
        # Take the first string and compare it with the other 
        # If one of the string of out bound we stop
        # If one of the string not match we stop
        # Otherwise we add it 