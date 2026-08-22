class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # What if i cannot use startswith()?
        def prefixCheck(lastPrefix, curWord):
            target = lastPrefix + "/"

            if len(curWord) < len(target):
                return False
            
            for i in range(len(target)):
                if target[i] != curWord[i]:
                    return False
            
            return True

        folder.sort()

        lastPrefix = folder[0]
        result = [folder[0]]

        for word in folder[1:]:
            # Why + "/" by the end?
            # To avoid compare: "a/b/c" with "a/b/ce"
            # They are not subfolder so that's why we compared:
            # Was "a/b/ce" start with "a/b/c/"?
            if not prefixCheck(lastPrefix, word):
                result.append(word)
                lastPrefix = word
        
        return result