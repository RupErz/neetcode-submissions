class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # #Sol 1 : Work but not optimal 
        # #Time : O(k * N) a loop : N, each loop using max on k elements => N * k => O(N)
        # size = len(nums)
        # if size < k : 
        #     return []
        # elif size == k :
        #     return [max(nums)]
        # else : 
        #     l = 0
        #     res = []
        #     for r in range(k - 1, size):
        #         res.append(max(nums[l:r + 1]))
        #         l += 1
        #     return res

        #Optimal : Time :O(N)
        output = []
        d = collections.deque()
        l = r = 0
        while r < len(nums):
            #Before adding anything to our d remember:
            # Maintaining "monotonic decreasing sequence"
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r) #Instead of storing value, we go "INDEX"
            #When do we have a valid window ?
            if r + 1 >= k : #after r reach this , we will always have valid
            #window in those loop after
                output.append(nums[d[0]])
                l += 1
            #And then we need to pop out deque since we alr move our left ?
            if l > d[0]:
                d.popleft() #Remove left most value from deque
            r += 1
        return output

