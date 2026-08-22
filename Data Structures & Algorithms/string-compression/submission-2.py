class Solution:
    def compress(self, chars: List[str]) -> int:
        # Assignment: You have an array "chars", compress into a string
        # like "a5b2c10" with length k = 9, rewrite directly into the 
        # array "chars" with exactly 9 elements then return the length 
        # of the array being written into
        # e.g: [a, a, b, c, c] => a2bc2 
        # => [a, 2, b, c, 2]

        # Hint / Advice:
        # Space O(1) do not create a string / list
        # 2 varialbe to : count the freq, position to insert
        # Modify the list IN PLACE
        # Don't forget the last trailing group

        count = 1 # Count the freq
        l = 0 # Position to write

        for r in range(1, len(chars)):
            if chars[r - 1] == chars[r]:
                count += 1
            else:
                chars[l] = chars[r - 1]
                l += 1
                if count > 1:
                    for i in str(count):
                        chars[l] = i
                        l += 1
                count = 1
        
        # Handle the last group
        chars[l] = chars[-1]
        l += 1
        if count > 1:
            for i in str(count):
                chars[l] = i
                l += 1

        return l # index 0 so left pointer is at the size of compress string
                
