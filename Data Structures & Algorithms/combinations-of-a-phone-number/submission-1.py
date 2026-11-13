class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': "abc",
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if len(digits) == 0:
            return []
        
        result = []
        def dfs(cur, curWord):
            if cur >= len(digits):
                result.append(curWord)
                return 
            
            for c in letters[digits[cur]]:
                dfs(cur + 1, curWord + c)
            
        dfs(0, "")
        return result



        
