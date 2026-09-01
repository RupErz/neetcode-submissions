# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1 Length - n = node to remove while iterating 
        length = 0

        cur = head
        while cur:
            length +=1
            cur = cur.next
        
        target = length - n

        curN = head

        if target == 0:
            return head.next # Removing that first element

        while curN:
            target -= 1
            if target == 0:
                curN.next = curN.next.next
                break
            
            curN = curN.next

        return head

