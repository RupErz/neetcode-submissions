class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.last = True

    def search(self, word: str) -> bool:
        def dfs(j, current):
            cur = current
            for i in range(j, len(word)):
                w = word[i]
                if w == ".":
                    # Using dfs exploring 26 possible path from here
                    for child in cur.children.values():
                        # If we can find a possible path
                        if dfs(i + 1, child):
                            return True 
                    # After all possible path, not once can be a valid
                    return False 
                else:
                    if w not in cur.children:
                        return False
                    cur = cur.children[w]
            return cur.last # Check whether they are last or not
        return dfs(0, self.root)
        
