class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dict = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

        # Why we dont use copy , cause str wont work and since we
        # have a 2nd variable , we dont need to use it.
        # a str pop woulbe quite time consuming .
        def backtrack (i, cur):
            if i >= len(digits):
                res.append(cur)
                return 
            
            for n in dict[digits[i]]:
                backtrack(i + 1, cur + n)
        if digits : # if empty it will be [""] should be [] instead
            backtrack(0, "")
        return res
        # Time : Worst case : N * 4 ^N