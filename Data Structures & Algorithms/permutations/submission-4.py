class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Iteration
        curPerms = [[]]
        for n in nums:
            nextPerms = [] 

            for p in curPerms:
                for j in range(len(p) + 1):
                    copyPerm = p.copy()
                    copyPerm.insert(j, n)
                    nextPerms.append(copyPerm)

            curPerms = nextPerms
        return curPerms