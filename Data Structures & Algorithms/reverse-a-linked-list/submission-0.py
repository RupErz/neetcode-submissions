# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # #Time O(N), Memory O(1)
        # prev, curr = None, head

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     #Because right after we point to this , we lost connection
        #     # with the next node
        #     prev = curr
        #     curr = nxt
        # #Since after reverse , the curr at NULL, prev at new HEAD
        # #we simply return ptr to our new head -> linkedlist
        # return prev

        #SOl2: LinkedList
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead