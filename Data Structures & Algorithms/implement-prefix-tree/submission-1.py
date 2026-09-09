# Create a tree node to support this Trie (a tree always need nodes)
class TreeNode:
    def __init__(self):
        self.nei = {} #Key: its nei char, value is the pointer to get to the nei
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        # Check root starting words
        # -> if not existed, add one by one, mark end for last w
        # -> existed, just follow up and mark end for last w
        cur = self.root
        for w in word:
            if w not in cur.nei:
                cur.nei[w] = TreeNode()
            cur = cur.nei[w]
        cur.end = True # mark as a finished words added

    def search(self, word: str) -> bool:
        # Check root and follow the pointer and check the mark end value
        # mark True return true
        # mark False return False 
        cur = self.root
        for w in word:
            if w not in cur.nei:
                return False
            cur = cur.nei[w]
        if cur.end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        # check if the string is existed in any string and it have to be 
        # a complete word (mark True by the end)
        # cur = self.root
        cur = self.root
        for w in prefix:
            if w not in cur.nei:
                return False
            cur = cur.nei[w]
        
        return True

        
        