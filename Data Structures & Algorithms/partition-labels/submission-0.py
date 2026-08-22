class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        # Hashmap track the last idx of each letter
        for i in range(len(s)):
            curLetter = s[i]
            last[curLetter] = i

        # we know it always have at least 1 val
        end = last[s[0]]
        result = []
        l = 0
        for r in range(len(s)):

            # We finish 1 substring
            if r == end:
                result.append(r - l + 1)
                l = r + 1
                # Settle new end 
                end = last[s[l]] if l < len(s) else float("inf")

            # We keep expand our end
            else:
                letter = s[r]
                end = max(end, last[letter])

        return result






