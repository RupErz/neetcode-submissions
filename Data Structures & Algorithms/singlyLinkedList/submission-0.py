class ListNode:
    def __init__(self, val):
        self.next = None
        self.value = val

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current != None: 
            if count == index:
                return current.value
            else: 
                count += 1
                current = current.next
        return -1


    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        if (self.head != None) :
            newNode.next = self.head
            self.head = newNode
        else :
            self.head = newNode
            self.tail = newNode


    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if (self.head != None) :
            self.tail.next =  newNode
            self.tail = newNode 
        else : 
            self.head = newNode
            self.tail = newNode


    def remove(self, index: int) -> bool:
        count = 0
        cur = self.head
        prev = None 

        # 1st: Remove the last item in the linkedlist : index 0 
        # 2nd: Remove the head : index 0 
        # 3rd: Remove the tail : cur = tail
        # 4th: Remove the middle node

        # Remove at first index
        if index == 0 :
            # If head have at least 1 node
            if self.head :
                self.head = self.head.next
                # If head is None after upd -> Only 1 node
                if not self.head:
                    self.tail = None
                return True
            return False
        
        while count < index and cur:
            count += 1
            prev = cur
            cur = cur.next
        
        # If index is within our range
        if cur :
            # Remove the tail
            if cur == self.tail:
                self.tail = prev
                prev.next = None
            else: 
                prev.next = cur.next
            return True
        return False




                

    def getValues(self) -> List[int]:
        current = self.head
        res = [] 
        while current != None :
            res.append(current.value)
            current = current.next
        return res
        
