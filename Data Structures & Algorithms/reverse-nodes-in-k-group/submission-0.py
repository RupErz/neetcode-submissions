# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # We gonna have a pointer to the node before 1st node to reverse
        # 2 nd ptr to point to the node next to the final node to reverse
        # a node to mark the stop of our reverse technique 
        groupPrev = dummy

        while True:
            kth = self.findKNode(groupPrev, k)
            if not kth : # k is Null
                break # We dont reverse and return res
            else :
                groupNext = kth.next
                #reverse 
                prev, cur = kth.next, groupPrev.next
                # ? : Why using kth.next making error occur ?
# => assume k point to a node 3( 2 -> 3), when we revere , we will put 3 -> 2
# which is also kth.next , so our stop point will be "modified" => error.
                while cur != groupNext: 
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                
                tmp = groupPrev.next # Which will be our next groupPrev
                groupPrev.next = kth
                groupPrev = tmp
        return dummy.next

    def findKNode(self, cur , k):
        while cur and k > 0 :
            cur = cur.next
            k -= 1
        return cur 
        # Meaning that if cur return Null we break the loop since we reach
        # the end and dont reverse the rest.
