class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordIndex = -1 # Last char will have index != -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Construct the trie with the pool of words
        root = TrieNode()
        for i in range(len(words)):
            word = words[i]
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.wordIndex = i # Mark current word index for future use
        
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(board), len(board[0])
        result = []

        # DFS logic
        def dfs(r, c, root, visited):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited:
                return

            # Cur char in the board
            curChar = board[r][c]

            # Cant find any word to start with - Stop
            if curChar not in root.children:
                return 
            
            # If we found a word to start with - Move
            nextNode = root.children[curChar]

            # If this node is the last = we find 1 word
            if nextNode.wordIndex != -1:
                result.append(words[nextNode.wordIndex])
                # In case the board have multiple "cat"
                nextNode.wordIndex = -1 
            
            visited.add((r, c))
            for nr, nc in DIRECTIONS:
                dfs(r + nr, c + nc, nextNode, visited)
            visited.remove((r, c))

        # Traversing through the board 
        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = set()
                dfs(r, c, root, visited)
        
        return result
        

        

            