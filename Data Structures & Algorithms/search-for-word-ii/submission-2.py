class TrieNode():
    def __init__(self):
        self.nei = {}
        self.end = False
        self.word = None


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for w in word:
            if w not in cur.nei:
                cur.nei[w] = TrieNode()
            cur = cur.nei[w]
        cur.end = True
        cur.word = word # Store for each word that is an end
    
    def search(self, word):
        cur = self.root
        for w in word:
            if w not in cur.nei:
                return False
            cur = cur.nei[w]
        return True if cur.end else False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Loop on each word and DFS on the entire board to find it repeating until the loop end. => Super upper inefficient 
        # 2? We must loop the words string meaning looping word by word
        trie = Trie()

        # Filling the tree with words
        for w in words:
            trie.add(w)
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        final = []

        def dfs(r, c, cur):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or board[r][c] not in cur.nei:
                return

            nextnode = cur.nei[board[r][c]]
            if nextnode.end:
                final.append(nextnode.word)
                nextnode.end = False# wipe it to avoid readding

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, nextnode)
            visited.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie.root.nei:
                    dfs(r, c, trie.root)

        return final

