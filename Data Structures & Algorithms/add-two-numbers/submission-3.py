# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1, cur2 = l1, l2
        dummy = ListNode()
        cur = dummy
        remain = 0

        while cur1 or cur2 or remain != 0:
            cur1Val = cur1.val if cur1 else 0
            cur2Val = cur2.val if cur2 else 0

            total = cur1Val + cur2Val + remain

            if total > 9:
                cur.next = ListNode(total % 10)
                remain = 1
            else:
                cur.next = ListNode(total)
                remain = 0
            
            cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        
        return dummy.next
            
        
        