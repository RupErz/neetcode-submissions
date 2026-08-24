class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # -1 0  0  0  0 product from L to R
        #  0 0  6  6  3 product from R to L 

        #  1  2  8  48
        #  48 48 24 6

        # Calculate the product from Left to Right
        LtoR = []
        curProdL = 1
        for i in range(len(nums)):
            LtoR.append(curProdL * nums[i])
            curProdL *= nums[i]
        
        # Cal prod from Right to Left
        RtoL = []
        curProdR = 1
        for i in range(len(nums) - 1, -1, -1):
            RtoL.append(curProdR * nums[i])
            curProdR *= nums[i]
        RtoL.reverse()
        
        final = []
        for i in range(len(nums)):
            left = LtoR[i - 1] if i - 1 >= 0 else 1
            right = RtoL[i + 1] if i + 1 < len(RtoL) else 1
            final.append(left * right)
    
        return final 



        
        

