class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
         
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curSize = 0
        self.lru = Node()
        self.mru = Node()
        self.task = {}
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if key in self.task:
            result = self.task[key].val

            # update its position to MRU 
            cur = self.task[key]
            nextCur = cur.next
            prevCur = cur.prev
            nextCur.prev = prevCur
            prevCur.next = nextCur

            # Then push to mru
            tmp = self.mru.prev
            cur.next = self.mru
            cur.prev = tmp
            tmp.next = cur
            self.mru.prev = cur

            return result
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.task:
            self.task[key].val = value

            # update its position to MRU 
            cur = self.task[key]
            nextCur = cur.next
            prevCur = cur.prev
            nextCur.prev = prevCur
            prevCur.next = nextCur

            # Then push to mru
            tmp = self.mru.prev
            cur.next = self.mru
            cur.prev = tmp
            tmp.next = cur
            self.mru.prev = cur

        else:
            if self.curSize == self.cap:
                toRemove = self.lru.next
                nextToRemove = toRemove.next
                self.lru.next = nextToRemove
                nextToRemove.prev = self.lru
                del self.task[toRemove.key]
                self.curSize -= 1

            newNode = Node(key, value)
            self.task[key] = newNode
            tmp = self.mru.prev
            newNode.next = self.mru
            newNode.prev = tmp
            tmp.next = newNode
            self.mru.prev = newNode
            self.curSize += 1

