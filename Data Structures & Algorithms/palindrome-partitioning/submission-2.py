class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def checkPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def dfs(curStart, curNow, curList):
            if curNow == len(s):
                result.append(curList.copy())
                return 
            
            # cut or keep
            # If we cut we have to check if the current substr is palindrome
            if checkPalindrome(curStart, curNow):
                curList.append(s[curStart : curNow + 1])
                dfs(curNow + 1, curNow + 1, curList)
                curList.pop()
            
            if curNow + 1 < len(s):
                dfs(curStart, curNow + 1, curList)

        dfs(0, 0, [])
        return result 
                
            
                

        