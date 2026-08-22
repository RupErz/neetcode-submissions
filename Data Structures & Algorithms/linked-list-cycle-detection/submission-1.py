# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Time O(N) Space: O(N)
        # nodePassed = set()
        # cur = head
        # while cur :
        #     if cur not in nodePassed:
        #         nodePassed.add(cur)
        #     else: 
        #         return True
        #     cur = cur.next
        # return False

        #Time: O(N) Space: O(1)
        slow, fast = head, head
        while fast and fast.next: #stop if fast reach Null or if next node of fast 
        # is Null cause if we even iterate fast still end up Null
            slow = slow.next
            fast = fast.next.next # Required fast.next != Null
            if slow == fast:
                return True
        return False
