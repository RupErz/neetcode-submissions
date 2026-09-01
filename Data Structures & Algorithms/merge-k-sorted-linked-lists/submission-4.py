# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Brute force
        # pop 2 each at a time
        # we perform merge 2 linked list then we push back 
        # keep continuing until the list len is 1 and cannot perform any merge 

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                l12 = self.merge(l1, l2)
                merged.append(l12)
            lists = merged
        
        return lists[0] if len(lists) == 1 else None


        
    def merge(self, ptrA, ptrB):
        dummy = ListNode()
        cur = dummy

        while ptrA and ptrB:
            valA = ptrA.val
            valB = ptrB.val
            if valA > valB:
                cur.next = ptrB
                ptrB = ptrB.next
            else:
                cur.next = ptrA
                ptrA = ptrA.next
            cur = cur.next
        
        if ptrA:
            cur.next = ptrA
        else:
            cur.next = ptrB 
        
        return dummy.next # ptr of a new merge linked list
        