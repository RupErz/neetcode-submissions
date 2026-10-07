class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = {}

        for w in wordList:
            for i in range(len(w)):
                pattern = w[0:i] + "*" + w[i + 1:]
                if pattern not in patterns:
                    patterns[pattern] = []
                patterns[pattern].append(w)
                

        bfs = deque()
        result = 1
        bfs.appendleft(beginWord)
        visited = set()

        while bfs:
            for i in range(len(bfs)):
                cur = bfs.pop()
                if cur == endWord:
                    return result
                visited.add(cur)

                # Generate cur pattern
                for i in range(len(cur)):
                    pattern = cur[0:i] + "*" + cur[i + 1:]
                    if pattern in patterns:
                        for word in patterns[pattern]:
                            if word not in visited:
                                bfs.appendleft(word)
            result += 1
        
        return 0



