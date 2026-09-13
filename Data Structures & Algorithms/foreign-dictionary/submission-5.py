class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # a list been sorted to alien language
        # return "" if invalid order
        # return "unique_letter" in ASC
        adj = {c:[] for w in words for c in w}
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]

            j, k = 0, 0
            while j < len(first) and k < len(second):
                if first[j] != second[k]:
                    adj[first[j]].append(second[k])
                    break
                j += 1
                k += 1
            
            # Stop when s or j out of bounds and that means f = s
            # That means f suppose to be SMALLER than s
            if j == min(len(first), len(second)) and len(first) > len(second):
                print("prefix fail", first, second)
                return ""
        
        print(adj)

        visited = {}
        result = []
        def dfs(cur):
            if cur in visited:
                return visited[cur] == False

            visited[cur] = True
            for nei in adj[cur]:
                if not dfs(nei):
                    return False
            visited[cur] = False
            result.append(cur)

            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        print(adj)
        print(result)
        result.reverse()
        return "".join(result)

            




       