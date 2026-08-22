# Array : O(N)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if self.head:
            return False
        return True

    # 2 case : When empty and not empty
    # New node : next is N, prev is 
    def append(self, value: int) -> None:
        newValue = Node(value)
        if (not self.head):
            self.head = newValue
        else:
            self.tail.next = newValue
            # Upd newNode previous
            newValue.prev = self.tail
        self.tail = newValue
        
    # 2 case : empty or not empty
    # New node : next is , prev is N
    def appendleft(self, value: int) -> None:
        newValue = Node(value)
        if (not self.head):
            self.tail = newValue
        else:
            newValue.next = self.head
            self.head.prev = newValue
        self.head = newValue

    # 2 case: 1 node or >= 1 node
    def pop(self) -> int:
        result = -1
        if not self.isEmpty():
            result = self.tail.value
            if (self.tail == self.head) :
                self.head = None
            self.tail = self.tail.prev
            if (self.tail):
                self.tail.next = None
        return result

    def popleft(self) -> int:
        result = -1
        if not self.isEmpty():
            result = self.head.value
            if (self.head == self.tail):
                self.tail = None
            self.head = self.head.next
            if (self.head):
                self.head.prev = None
        return result
