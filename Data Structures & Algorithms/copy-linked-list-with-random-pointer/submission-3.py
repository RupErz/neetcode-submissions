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
        cur = head
        copies = {}

        # Making a copy node with value only 
        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            copies[cur].next = copies.get(cur.next, None)
            copies[cur].random = copies.get(cur.random, None)

            cur = cur.next
        
        return copies[head] if head else None


        
        