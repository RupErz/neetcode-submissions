class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # vd: [1, 10 , 5, 20] we will add a 0 to the end
        # [1, 10, 5, 20, 0]
        # [0, 1, 2, 3, 4] : index
        # at idx 3 and 4 nothing we need to change !
        # So we start at idx2

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1) :
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])