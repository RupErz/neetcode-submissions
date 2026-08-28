class Solution:
    def isValid(self, s: str) -> bool:
        # Brackets = Stack
        opens = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        order = []
        for br in s:
            if br in opens:
                order.append(br)
            else:
                if order:
                    openbr = order.pop()
                    if br != opens[openbr]:
                        return False
                else:
                    return False
        
        return True if len(order) == 0 else False



