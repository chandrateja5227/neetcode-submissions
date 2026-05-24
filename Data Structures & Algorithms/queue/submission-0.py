class Node:
    def __init__(self,value:int):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False
        
    def append(self, value: int) -> None:
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        
    def pop(self) -> int:
        if self.tail is None:
            return -1
        else:
            node = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return node.value
        

    def popleft(self) -> int:
        if self.head is None:
            return -1
        else:
            node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return node.value
