class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair of index and height
        # [ [index start, height ] ]

        for i,h in enumerate(heights):
            start = i #use to track possible backward to the left

            #If it's lower , meaning that we can pop and update our current strt
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx #Since our previous is higher , so we can go left

            #If next element > previous on the stack
            #That means we can't lengthen to the left !
            #So start will be at our index i
            stack.append((start, h)) #list can only add 1 item at a time!

        #After the loop there will still some value in the stack, so we 
        #need to calculate all of them 
        for idx, height in stack :
            #Since these are rectangle that follow until the end:
            maxArea = max(maxArea, height * (len(heights) - idx))
        return maxArea

