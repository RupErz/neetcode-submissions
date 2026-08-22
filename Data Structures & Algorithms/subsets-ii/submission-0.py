class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Find the ss with high dmg + atk sup
        # sort the list : need to skip element
        nums.sort()

        def backtrack(i, cur) : #index to move on, current subset
            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)

            # not chosen 
            cur.pop()
            # if not choose this ele, we have to skip remember?
            # Make sure i + 1 is existed => Error
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, cur)
        backtrack(0, [])
        return res
            
