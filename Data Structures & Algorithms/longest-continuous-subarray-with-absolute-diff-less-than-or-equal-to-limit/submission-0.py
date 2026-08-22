class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Subarray -> Sliding window
        if len(nums) == 0:
            return 0

        l = 0

        # 2 monotonic deque storing index

        maxQ = deque() # Inc order (front = max)
        # lowest - highest

        minQ = deque() # Dec order (front = min)
        # highest - lowest
        
        result = 0

        for r in range(len(nums)):
            nextVal = nums[r]

            # Maintain maxQ
            while maxQ and nextVal < nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(r)

            # Maintain minQ
            while minQ and nextVal > nums[minQ[-1]]:
                minQ.pop()
            minQ.append(r)

            while minQ and maxQ and abs(nums[maxQ[0]] - nums[minQ[0]]) > limit:
                # Shrink it 
                l += 1

                if l > maxQ[0]:
                    maxQ.popleft()
                if l > minQ[0]:
                    minQ.popleft()
                
            result = max(result, r - l + 1)
        return result
                
                



           
