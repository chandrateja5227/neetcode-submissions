class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_end(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self._move_to_end(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self._move_to_end(node)
        else:
            if len(self.hash_map) == self.capacity:
                lru = self.head.next
                del self.hash_map[lru.key]
                self.head.next = lru.next
                lru.next.prev = self.head
            
            new_node = ListNode(key, value, self.tail.prev, self.tail)
            self.hash_map[key] = new_node
            self.tail.prev.next = new_node
            self.tail.prev = new_node