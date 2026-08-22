# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 2 edge case : When list is empty and 
        if len(lists) < 1 or not lists:
            return None

        # We will perform merge sort : O(n * log K)
        while len(lists) > 1:
            mergeList = [] # a dummy list so we can update our lists later

            for i in range(0, len(lists), 2): # Why 2 : We take 2 list to merge each time
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None # vd: [[1,2][3][4]]
                mergeList.append(self.mergelist(list1, list2))
            lists = mergeList #Update into newest list
        return lists[0] if list[0] else None

    def mergelist(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        # Stop when 1 of the list reach the end or Null
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            if val1 > val2:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1: # if cur1 still have => cur2 alr Null
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next 
            
