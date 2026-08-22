# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None 
        # cur = l1
        # while cur :
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        #=> New ptr is prev : ptr of reverse list
        cur1 = l1
        cur2 = l2
        num1 = []
        num2 = []
        while cur1:
            num1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            num2.append(cur2.val)
            cur2 = cur2.next
        num1 = int("".join(map(str, num1[::-1])))
        num2 = int("".join(map(str, num2[::-1])))
        sum = str(num1 + num2)[::-1]
        
        dummy = ListNode()
        current = dummy
        for num in sum:
            current.next = ListNode(num)
            current = current.next

        return dummy.next




