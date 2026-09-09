class TreeNode():
    def __init__(self):
        self.nei = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.nei:
                cur.nei[w] = TreeNode()
            cur = cur.nei[w]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i == len(word):
                return cur.end

            if word[i] == ".":
                for nc in cur.nei.values():
                    if dfs(nc, i + 1):
                        return True
                return False 
            else:
                if word[i] not in cur.nei:
                    return False
                return dfs(cur.nei[word[i]], i + 1)

        return dfs(self.root, 0)
















