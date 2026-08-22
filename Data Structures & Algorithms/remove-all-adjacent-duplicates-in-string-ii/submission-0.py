class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Stack : ).
        adj = []

        for i in range(len(s)):
            curChar = s[i]

            if adj:
                prevChar, count = adj.pop()
                # If they are equal : check if count + 1 reach k
                if prevChar == curChar:
                    if count + 1 != k:
                        adj.append((curChar, count + 1))

                # If they are not equal : add directly to stack
                else:
                    adj.append((prevChar, count))
                    adj.append((curChar, 1))
            else:
                adj.append((curChar, 1))
        

        result = ""
        for i in range(len(adj)):
            letter, amount = adj[i]
            result += letter * amount
        return result

        
        
        
            


