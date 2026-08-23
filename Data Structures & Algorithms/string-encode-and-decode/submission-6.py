class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for w in strs:
            encoded = str(len(w)) + "#" + w
            result += encoded
        return result

        #   5#Hello5#World <- After Encode
        # Decoder: Hello, World oh my

    # Why # ? 256 ascii have NUMBER too so it can be "7Hello"
# a b 
# 5#Hello5#World i = 1 -> 6 (1, )
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            size = int(s[i:j])
            i = j + 1 # Move to position to add
            j = i + size

            subStr = s[i:j]
            res.append(subStr)
            i = j

        return res        