class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count = {}
        for i in hand:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        for i in hand:
            if i not in count:
                continue
            for j in range(i, i + groupSize, 1):
                if j not in count:
                    return False
                count[j] -= 1
                if count[j] == 0:
                    del count[j]
                
        return True