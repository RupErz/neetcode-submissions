# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        # if 1 of head Null -> assume its zero
        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            #Now we extract into number and carry
            # 1 digit + 1 digit always < 99
            res = sum % 10 #vd: 15 % 10 = 5
            carry = sum // 10 #vd : 15 // 10 = 1 , 25 // 10 = 2
            current.next = ListNode(res)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next