class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # Create an adjacency list:
        q = deque()
        q.append("0000")
        visited = set()
        visited.add("0000")
        avoid = set(deadends)
        result = 0

        if "0000" in deadends:
            return -1
        while q:
            for i in range(len(q)):
                curCode = q.popleft()
                if curCode == target:
                    return result

                for j in range(len(curCode)):
                    curDigit = int(curCode[j])
                    goUp = (curDigit + 1) % 10
                    goDown = (curDigit - 1) % 10

                    patternUp = curCode[:j] + str(goUp) + curCode[j + 1:]
                    patternDown = curCode[:j] + str(goDown) + curCode[j + 1:]

                    if patternUp not in avoid and patternUp not in visited:
                        q.append(patternUp)
                        visited.add(patternUp)
                    
                    if patternDown not in avoid and patternDown not in visited:
                        q.append(patternDown)
                        visited.add(patternDown)
                
            result += 1
            
        return -1



