class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = {}

        # Traverse through the string to get the stop point of each letter 
        for i in range(len(s)):
            cur = s[i]
            end[cur] = i

        result = []
        l, r = 0, end[s[0]]
        i = 0
        while i in range(len(s)):
            if i < r:
                r = max(r, end[s[i]])
            else:
                result.append(r - l + 1)
                if i + 1 < len(s):
                    l = i + 1
                    r = end[s[i + 1]]
                else:
                    break
            i += 1
        
        return result


        

            