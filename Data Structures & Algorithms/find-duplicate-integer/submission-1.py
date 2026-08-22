class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Definitely not the right answer ( although true )
        # Time O(N) Space : O(N)
        # hashSet = set()
        # for i in nums:
        #     if i in hashSet:
        #         return i
        #     else:
        #         hashSet.add(i)

        #Sol2 : Floy'd Algo
        #imagine our array into a linkedlist
        # idx : 0 1 2 3 4
        # val : 1 3 4 2 2 these are ptr (vd: val 1 -> idx 1)
        # Visualizing them into a real linkedlist

        slow, fast = 0, 0
        while True:
            #Move them until they encountered each other
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
