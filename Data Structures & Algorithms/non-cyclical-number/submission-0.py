class Solution:
    def isHappy(self, n: int) -> bool:
        # 100 % 10 = 0
        # 10 % 10 = 0
        # 1 % 10 = 1
        # 1 / 10 = 0. 1

        # set()
        # # Find the sum of square between digits ?
        #     1) convert to str, loop, convert back to int() , square it
        #     => ?
        #     2) 2 ** 2 
        
        visit = set()
        cur = n

        while cur not in visit:
            visit.add(cur)
            curSum = 0

            while cur >= 1:
                curSum += ((cur % 10) ** 2)
                cur = cur // 10
            
            if curSum == 1:
                return True
            
            cur = curSum
        
        return False
