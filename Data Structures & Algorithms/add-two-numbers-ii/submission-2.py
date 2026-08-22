# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # First solution (more practical compare to string conversion)
        # Reverse 2 linkedlist
        # Then prepend into a dummy node
        # Will be O(1) space if we not count the output list
        # Modifying the input is not ideal

        prev1 = None
        prev2 = None
        cur1 = l1
        cur2 = l2

        while cur1:
            tmp = cur1.next
            cur1.next = prev1
            prev1 = cur1
            cur1 = tmp
        
        while cur2:
            tmp = cur2.next
            cur2.next = prev2
            prev2 = cur2
            cur2 = tmp
        
        carry = 0
        dummy = ListNode()

        while prev1 or prev2 or carry:
            total = 0

            if prev1:
                total += prev1.val
                prev1 = prev1.next
            
            if prev2:
                total += prev2.val
                prev2 = prev2.next
            
            total += carry

            stored = total % 10
            carry = total // 10

            newNode = ListNode(stored)
            newNode.next = dummy.next
            dummy.next = newNode

        return dummy.next
        
        # Addition between 2 numbers => Right to Left operation
        # What DSA to prio rightmost number ? Stack.
        # Linkedlist Prepend ?
        # Avoid using str(num) int(str) -> Integer Overflow.

        # stack1 = []
        # stack2 = []

        # cur1 = l1
        # cur2 = l2

        # while cur1:
        #     stack1.append(cur1.val)
        #     cur1 = cur1.next

        # while cur2:
        #     stack2.append(cur2.val)
        #     cur2 = cur2.next
        
        # remainder = 0 # Can either 0 or 1
        # dummy = ListNode()

        # while stack1 or stack2 or remainder:
        #     total = 0

        #     if stack1:
        #         num1 = stack1.pop()
        #         total += num1

        #     if stack2:
        #         num2 = stack2.pop()
        #         total += num2

        #     total += remainder
        #     num3 = total % 10
        #     remainder = total // 10

        #     # Start Prepending into the result list
        #     newNode = ListNode(num3)
        #     newNode.next = dummy.next
        #     dummy.next = newNode 
        
        # return dummy.next

# dummy -> 0 -> Null
# A -> Null
# B -> Null
# A -> B
