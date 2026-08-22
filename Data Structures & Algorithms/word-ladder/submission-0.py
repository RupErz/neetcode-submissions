class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        
        # Try multiple ways

        # Transform into another word with 1 char diff

        # Repeat until reach the end

        # Return 0 when get stuck , cannot move forward

        # How to track which word to transform
        # hashmap with occurences?

        def diff(c1, c2):
            diff = 0
            for i in range(len(c1)):
                if c1[i] != c2[i]:
                    diff += 1

            return True if diff == 1 else False
        visited = set()

        def dfs(cur, visited):
            if cur in visited:
                return float("inf")

            if cur == endWord:
                return 1

            visited.add(cur)
            result = float("inf")

            for i in range(len(wordList)):
                nextWord = wordList[i]
                if cur != nextWord:
                    # Start checking if they are valid to transform
                    if diff(cur, nextWord):
                        choices = 1 + dfs(nextWord, visited)
                        if choices != float("inf"):
                            result = min(result, choices) 

            visited.remove(cur)
            return result

        goals = dfs(beginWord, visited)
        return goals if goals != float("inf") else 0





        