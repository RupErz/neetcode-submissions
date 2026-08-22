class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        lastPrefix = folder[0]
        result = [folder[0]]

        for word in folder[1:]:
            if not word.startswith(lastPrefix + "/"):
                result.append(word)
                lastPrefix = word
        
        return result