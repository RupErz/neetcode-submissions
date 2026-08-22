class Solution:
    def compress(self, chars: List[str]) -> int:
        # Constraints: O(1) space complexity 
        # Need to track if its fall into condition 1 or 2
        # C1: Only 1 char count
        # C2: More than 1 char count

        count = 1 # Count the freq
        l = 0 # Position to write
        result = 0 # Length of compress string

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
                result += 1
        
        # Handle the last group
        chars[l] = chars[-1]
        l += 1
        if count > 1:
            for i in str(count):
                chars[l] = i
                l += 1

        return l
                
