class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = (len(nums1) + len(nums2)) 
        half = total // 2 # Finding the number of left partition should be
        A, B = nums1, nums2
        # Just make sure A is smaller array
        if len(nums2) < len(nums1) :
            A, B = nums2, nums1

        l, r = 0, len(A) - 1
        # If we sure that we guarantee to have an outcome .
        while True :
            i = (l + r) // 2 # even if the small arr empty -> -1 / 2 = -1
            j = half - i - 2 # why -2 : its a formula to find index of big arr

            # Then we start finding our left , right partition 
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if i + 1 < len(A) else float('+infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if j + 1 < len(B) else float('+infinity')
            # BUT, what if i + 1 out of bounds ? -> We need to use +-inf to
            # take care of it .

            if Aleft <= Bright and Bleft <= Aright: 
                # It's a proper partition
                if total % 2 == 0 : 
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else :
                    return min(Aright, Bright)
            elif Aleft > Bright :
                r = i - 1
            else :
                l = i + 1
            