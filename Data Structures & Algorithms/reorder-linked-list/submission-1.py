# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Finding middle w F+S
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reversing the second half 
        
        cur = slow.next
        prev = None 
        slow.next = None # Cut the end point of first half 

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        secondHalf = prev

        # Merging the 2 linked list altogether
        #  0 1 2 3 <- a   4 5 6 <- b
        cur = head
        while secondHalf:
            tmp = cur.next
            tmp2 = secondHalf.next

            cur.next = secondHalf
            secondHalf.next = tmp

            cur = tmp
            secondHalf = tmp2
        

