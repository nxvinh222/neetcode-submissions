class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def removeFromLinkedList(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def addToLinkedList(self, node: Node):
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.removeFromLinkedList(self.cache[key])
        self.addToLinkedList(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeFromLinkedList(self.cache[key])
        self.cache[key] = Node(key, value)
        self.addToLinkedList(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.removeFromLinkedList(lru)
            del self.cache[lru.key]