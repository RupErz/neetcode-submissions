class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i in range(len(s)):
            # If order is empty
            cur = s[i]
            if cur == "(":
                left.append(i)
            elif cur == "*":
                star.append(i)
            else:
                if not left and not star:
                    return False
                # Handle the case
                if left:
                    left.pop()
                else:
                    star.pop()

        # If both left and star still not empty
        while left:
            leftidx = left.pop()
            if not star:
                return False
            staridx = star.pop()
            if staridx < leftidx:
                return False

        return True # As long as left is empty star can turn empty 