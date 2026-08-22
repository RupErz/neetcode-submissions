# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        cur1 = l1
        cur2 = l2

        while cur1:
            stack1.append(cur1.val)
            cur1 = cur1.next

        while cur2:
            stack2.append(cur2.val)
            cur2 = cur2.next
        
        remainder = 0 # Can either 0 or 1
        dummy = ListNode()

        while stack1 or stack2 or remainder:
            total = 0

            if stack1:
                num1 = stack1.pop()
                total += num1

            if stack2:
                num2 = stack2.pop()
                total += num2

            total += remainder
            num3 = total % 10
            remainder = total // 10

            # Start Prepending into the result list
            newNode = ListNode(num3)
            newNode.next = dummy.next
            dummy.next = newNode 
        
        return dummy.next

# dummy -> 0 -> Null
# A -> Null
# B -> Null
# A -> B
