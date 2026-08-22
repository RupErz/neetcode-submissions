class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # 1 digit 
        # see non digit compare
        # see digit skip n words

        # 2 digit 
        # It's either 2 digit or Invalid e.g: i57 -> 57 or invalid
        # i012n -> i, 0 leading 0 so invalid
        # i0mplementation, i -> leading zero so no
        #     unless it's i10 
        
        l, r = 0, 0

        # As long as our ptr in abbr not out of bounds
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