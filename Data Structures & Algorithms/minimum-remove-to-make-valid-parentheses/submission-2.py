class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 2 pass technique
        # 1st pass to filter any invalid closing
        # 2nd pass to filter any invalid open parenthesis
        # 1 good thing really good when it comes to parenthesis
        # Using 1 varialbe count +1 if open -1 if close.

        # Reminder: We need to ensure "minimal" removal

        first = []
        cnt = 0
        for c in s:
            if c == "(":
                first.append(c)
                cnt += 1
            elif c == ")" and cnt > 0:
                first.append(c)
                cnt -= 1
            elif c != ")":
                first.append(c)
        
        # So now our first will may have "extra" open parenthesis
        # We need to do another pass to remove it.
        # Ideally we should remove the last invalid parenthesis
        # Why ? It guarantee we not violate any existed closing parenthesis

        filtered = []
        for c in first[::-1]:
            if c == "(" and cnt > 0:
                cnt -= 1
            else:
                filtered.append(c)
        filtered.reverse()
        return "".join(filtered)
