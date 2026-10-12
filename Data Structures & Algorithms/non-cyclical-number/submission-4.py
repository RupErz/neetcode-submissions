class Solution:
    def isHappy(self, n: int) -> bool:
        curNum = n
        visited = set()
        visited.add(curNum)

        while True:
            curNum = sum(int(d)** 2 for d in str(curNum))
            if curNum == 1:
                return True
                
            if curNum in visited:
                return False
            
            visited.add(curNum)

