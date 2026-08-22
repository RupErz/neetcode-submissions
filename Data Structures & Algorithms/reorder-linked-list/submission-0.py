# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next
        #We will stop when our fast ptr reach the end or out of bounds
        while fast and fast.next : #fast not null and fast next val not null
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next #Head ptr of second half

        slow.next = None #To break the link with the rest of node 
        #Now we have 2 separate linkedlist for first and second half.

        #Now we start reversing the second half linkedlist.
        prev = None
        while second :
            temp = second.next #Once we point our second.next to another val ,we lost
            #connection to our next node
            second.next = prev
            prev = second
            second = temp
        #After this , second -> None, prev is new head of our reverse list
        
        first, second = head, prev
        while second: #while second not null
            tempF = first.next
            tempS = second.next
            first.next = second
            second.next = tempF
            first = tempF
            second = tempS
