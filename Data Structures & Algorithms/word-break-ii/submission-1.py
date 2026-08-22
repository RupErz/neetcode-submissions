class TrieNode:
    def __init__(self):
        self.children = {} # a: TrieNode()
        self.last = False
        self.fullWord = ""
    
    def addNode(self, word): # O(1)
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.last = True
        cur.fullWord = word # Adjust so the node will store the complete word

    def searchNode(self, word): # O(1)
        cur = self
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.last # True if its an actual word False if not

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Trie (list of words to build - wordDict)
        # DFS () => Return all possible cases

        # Fill out the Trie with list of words
        root = TrieNode()
        for word in wordDict:
            root.addNode(word)
        
        result = []
        def dfs(i, sentence):
            if i == len(s):
                result.append(" ".join(sentence))
                return
            
            node = root # Reset to root meaning only recurse if we found 1 valid word

#             neetcode wordDict = [neet, code]
# n, e, e, t => a valid word then append [] then recurse at next starting index
#     c, o, d, e = a valid then append [] we reach base case , add it
# n, e, e, t => pop it start explore further to see any possible words e.g: neetar
#     if within child node "t" no word fit => break and stop
#     if within child node "t" word fit => continue exploring
# Note: Only recursion when we found a valid word

# The reason we use for indicating exploring futher path like case of : "race" , "racecar"
            for j in range(i, len(s)): 
                curWord = s[j]

                if curWord in node.children:
                    node = node.children[curWord]
                    # Check if it's the last word:
                    if node.last:
                        sentence.append(node.fullWord)
                        dfs(j + 1, sentence) # Take this word and recurse from this
                        sentence.pop() # Pop to start checking other cases
                    # If it's not last word then we just continue explore
                    # By going to the next loop j + 1
                else:
                    break

        dfs(0, [])
        return result



        
        

