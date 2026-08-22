class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # Recursion
        # # Time :  n! (permutations -dominant) * n^2 (operations in each permutation)
        # # ( insert into each spot )
        # # Space: n! * n ( multiple copies )
        # if len(nums) == 0 :
        #     return [[]]

        # res = []

        # # First we need to keep recurse until basecase 
        # perms = self.permute(nums[1:]) # omit the first value each time
        # # perms : number of permutations we current have e.g: [[2 ,3], [3, 2]]
        # for p in perms :
        #     for i in range(len(p) + 1): # because we need to access to the back
        #         copy = p.copy()
        #         copy.insert(i, nums[0])
        #         res.append(copy)
        # return res

        # Iteration 
        # Iteration have same pattern like recursion
        # Starting with 1 val , then 2 , then 3 follow up with its permutation
        perms = [[]]

        for n in nums : 
            cur = []
            for p in perms :
                for i in range(len(p) + 1): 
                    copy = p.copy()
                    copy.insert(i, n)
                    cur.append(copy)
            perms = cur
        return perms 


        