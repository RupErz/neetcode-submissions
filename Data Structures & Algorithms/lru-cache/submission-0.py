class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.physicalSize = capacity
        self.cache = {} # Map key to our node

        # left = LRU , right = Most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    #Remove the node
    def remove(self, node):
        previousNode = node.prev
        nextNode = node.next
        previousNode.next = nextNode
        nextNode.prev = previousNode

    #Add it to the right ( become most recently used )
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        #Connect prev with new node
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt

    #Everytime use get/put , the node used frequency changed
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        # If they put a same key :
        if key in self.cache :
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.physicalSize:
            #Remove the LRU ( Least recently used)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
