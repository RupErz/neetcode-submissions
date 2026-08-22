class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = {} # {pattern: [wordA, wordB]}
        wordList.append(beginWord)
        for i in range(len(wordList)):
            curWord = wordList[i]
            for j in range(len(curWord)):
                pattern = curWord[:j] + "*" + curWord[j + 1:]
                if pattern not in nei:
                    nei[pattern] = []
                nei[pattern].append(curWord)
        
        # Perform BFS
        visited = set(beginWord)
        q = deque()
        q.append(beginWord)
        res = 1

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
            
                # Adding all neighbors:
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)

            res += 1
        return 0
