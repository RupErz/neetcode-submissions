class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sort ??
        if len(hand) % groupSize != 0:
            return False # We dont have enough to separate evenly
        
        freq = Counter(hand)
        hand.sort()

        for num in hand:
            if freq[num]:
                start = num

                for i in range(start, start + groupSize):
                    if i not in freq:
                        return False
                    freq[i] -= 1
                    if freq[i] == 0:
                        del freq[i]
                
        
        return True
        # Time complexity: O(N^2) worst
        # Space: O(n)