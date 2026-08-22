class Solution:
    def convert(self, s: str, numRows: int) -> str:
        form = [ [""] * (len(s)) for _ in range(numRows)]
        isZigZag = False
        curRow, curCol = 0, 0

        # Move down : r + 1, c
        # Move zigzag : r - 1, c + 1

        for char in s:
            if isZigZag :
                form[curRow][curCol] = char
                if curRow - 1 < 0:
                    isZigZag = False
                    curRow += 1
                else:
                    curRow -= 1
                    curCol += 1
            else :
                form[curRow][curCol] = char
                if curRow + 1 == numRows:
                    isZigZag = True
                    curRow -= 1
                    curCol += 1
                else :
                    curRow += 1
        result = ""
        for r in range(len(form)):
            for c in range(len(form[0])):
                result += form[r][c]
        return result
                
