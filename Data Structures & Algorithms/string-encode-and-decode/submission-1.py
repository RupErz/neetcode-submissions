class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # We will encode as "3#lov1#a" : numb char to read/pound ( delim)/ read
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        # s here is coming from the string we encoded earlier
        res , i= [], 0
        # 2 ptrs : i point to the length str to read, j point to the pound sign
        while i < len(s):
            j = i #since after done reading 1 , i will point to the next length
            while s[j] != '#':
                j += 1
            # Why string slices ? In case the length over 1 digit : 1x
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length])
            i = j + 1 + length
        return res


        