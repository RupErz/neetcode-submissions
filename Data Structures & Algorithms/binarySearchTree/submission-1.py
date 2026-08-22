class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None 

class TreeMap:
    
    def __init__(self):
        self.head = None

    # Key is unique ! only > or < 
    # if another dup key -> override its value
    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if (not self.head):
            self.head = newNode # not current = newNode ,current just a ptr
            return
        current = self.head

        while True:
            if newNode.key < current.key:
                if (not current.left):
                    current.left = newNode
                    return # Exit the function
                current = current.left
            elif newNode.key > current.key:
                if (not current.right):
                    current.right = newNode
                    return
                current = current.right
            else :
                current.value = newNode.value
                return

    def get(self, key: int) -> int:
        current = self.head

        while current:
            if key > current.key:
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                break

        return current.value if current else -1



    def getMin(self) -> int:
        current = self.head
        if (not current):
            return -1
        while current.left:
            current = current.left
        return current.value


    def getMax(self) -> int:
        current = self.head
        if (not current):
            return -1
        while current.right:
            current = current.right
        return current.value

    def remove(self, key: int) -> None:
        self.head = self.removeHelper(self.head, key)

    # Return new Root at current subTree
    def removeHelper(self, curr, key):
        if (not curr):
            return None

        # Finding the target key / Indirectly remove node
        # in case 1 and 2: Leaf node and node with 1 child
        if curr.key > key:
            curr.left = self.removeHelper(curr.left, key)
        elif curr.key < key:
            curr.right = self.removeHelper(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
            # Remove the node with 2 children
            # Swap current with minNode at right subtree then del the leaf -> recursion
                minNode = self.findMin(curr.right)
                curr.key, curr.val = minNode.key, minNode.value
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    # Return the Node with minimum key in a subTree
    def findMin(self, curr):
        while curr.left:
            curr = curr.left
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        current = self.head

        def recursion(current):
            # Left Print Right : Inorder traversal
            if current:
                recursion(current.left)
                result.append(current.key)
                recursion(current.right)

        recursion(current)
        return result


