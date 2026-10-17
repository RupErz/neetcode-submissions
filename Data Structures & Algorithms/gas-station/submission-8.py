class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0
        i = 0
        while i < len(gas):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
            i += 1


        return start if total >= 0 else -1