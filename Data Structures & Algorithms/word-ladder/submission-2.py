class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
# Core behind this is for a word if you list out all of its possibilities
# with * : *at, b*t, ba*, you will see if 2 words will have 1 overlap pattern
# proving that they have 1 difference in words.

# From that we will form an adj list with key: pattern, value: word itself

# Finding minimum: BFS: Queue, Set(to avoid revisit)
# Once you have adj, finding neighbor of a current word is simple with SET and
# pattern
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

        # Time: O(n^2 * m) n is the len of the word, m is the list length
        # Space: O(n^2 * m)
