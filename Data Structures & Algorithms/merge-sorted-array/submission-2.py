class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Using 3 pointers, we merge backward ensure increasing order
        first = m - 1
        second = n - 1
        third = m + n - 1
        while first >= 0 and second >= 0:
            if nums1[first] > nums2[second]:
                nums1[third] = nums1[first]
                first -= 1
            else:
                nums1[third] = nums2[second]
                second -= 1
            third -= 1
        # 10, 20, 10, 20, 20, 40  
        # Check which one is empty which one not 
        if first < 0:
            while second >= 0:
                nums1[third] = nums2[second]
                second -= 1
                third -= 1
        