# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        #We dont need to change our head since we dont need to track dummy node
        l,r = dummy,head
        while n > 0 and r :
            r = r.next
            n -= 1

        while r :
            l = l.next
            r = r.next
        #Delete the node
        l.next = l.next.next
        return dummy.next
        #Time : O(N)

                
