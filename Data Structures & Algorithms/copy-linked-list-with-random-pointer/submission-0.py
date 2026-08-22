"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Time : O(N)
        #Using a hashmap to store our node
        # We store the pointer to node in org list as a key 
        #WHY? When we assign random pointers , make sure there always a
        # reference to our node => 2 Loop
        #1st : Create clone node , no link
        #2nd : Start linking our node
        hashMap = {None : None} #When update next ptr, if it was None -> None
        

        cur = head
        while cur:
            hashMap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            hashMap[cur].next = hashMap[cur.next]  #handle this None case line 19
            hashMap[cur].random = hashMap[cur.random]
            cur = cur.next

        return hashMap[head] #Since we alr record all pointers ref as a key
        