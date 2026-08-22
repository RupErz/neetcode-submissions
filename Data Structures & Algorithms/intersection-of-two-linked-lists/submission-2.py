# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Both pointer go m + n nodes
        # So by the end they will end up at Null at the SAME TIME
            # If there are no intersection
        # So if there are intersection they will catch up at 1 point
        # Space: O(1)

        curA = headA
        curB = headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA