class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sort ??
        if len(hand) % groupSize != 0:
            return False # We dont have enough to separate evenly
        
        groups = len(hand) // groupSize
        freq = Counter(hand)

        while groups > 0:
            start = min(freq.keys())

            for i in range(start, start + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
                
            groups -= 1
        
        return True
        # Time complexity: O(N)
        # Space: O(n)
        # each group: groups * (n + groupSize) 