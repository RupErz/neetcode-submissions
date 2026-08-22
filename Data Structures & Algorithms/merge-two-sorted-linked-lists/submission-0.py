# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Create a dummy node
        dummy = ListNode() #So dummy is a node right
        tail = dummy

        while list1 and list2 : #non null
            if list1.val < list2.val :
                tail.next = list1 #tail.next = dummy node
                list1 = list1.next
            else :
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1 # Insert the remaining list into our tail
            list1 = None
        else :
            tail.next = list2
            list2 = None
        return dummy.next #imagine dummy as a head


            
