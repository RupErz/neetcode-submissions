class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # i = 0 (1, 2) x
    # i = 1 (2, 2) o                    
    # i = 2 (3, 4) x        
    # i = 3 (4, 1) o
    # ?) Was highest gas station meaning it enough to go next n + 1?

        if sum(gas) < sum(cost):
            return -1

        # Greedy on "total net" NOT the starting GAS amount
        curTank, index = 0, 0
        
        for i in range(len(gas)):
            curTank += (gas[i] - cost[i])
            if curTank < 0:
                curTank = 0
                index = i + 1
        
        return index if index < len(gas) else -1
        
            