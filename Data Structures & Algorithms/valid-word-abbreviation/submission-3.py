class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # See digit ? Check for consecutive numbers since it cannot be 2 different numbers stand next to each other (violate)
        # Edge Case: leading 0
        # See nondigit ? Check if they are match and increment 2 pointer
        # True when each pointer reach its string length False otherwise
        l, r = 0, 0

        while r < len(abbr) and l < len(word):
            curChar = word[l]
            curAbbr = abbr[r]

            if curAbbr.isdigit():
                while r + 1 < len(abbr) and abbr[r + 1].isdigit():
                    curAbbr += abbr[r + 1]
                    r += 1

                if curAbbr[0] == "0":
                    return False
                
                # Skip x char based on the number:
                for i in range(int(curAbbr)):
                    l += 1
                    
                r += 1
            else:
                if curChar != curAbbr:
                    return False
                l += 1
                r += 1

        return True if l == len(word) and r == len(abbr) else False