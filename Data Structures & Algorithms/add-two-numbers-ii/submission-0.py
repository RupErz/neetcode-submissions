# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        string1 = ""
        string2 = ""

        while cur1:
            string1 += str(cur1.val)
            cur1 = cur1.next
        
        while cur2:
            string2 += str(cur2.val)
            cur2 = cur2.next
        
        result = int(string1) + int(string2)

        dummy = ListNode()
        cur = dummy
        for num in str(result):
            cur.next = ListNode(num)
            cur = cur.next
        
        return dummy.next