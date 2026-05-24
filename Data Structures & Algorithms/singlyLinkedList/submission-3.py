from typing import List, Optional

class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.pointer: Optional[Node] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def get(self, index: int) -> int:
        i = 0
        node = self.head
        while node is not None and i < index:
            node = node.pointer
            i += 1
        if node is None:
            return -1
        else:
            return node.value

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.pointer = self.head
        self.head = node
        if self.tail is None:  # Empty list before insert
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        node.pointer = None
        if self.tail is None:  # Empty list
            self.head = node
            self.tail = node
        else:
            self.tail.pointer = node
            self.tail = node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.pointer
            if self.head is None:
                self.tail = None
            return True
        i = 0
        node = self.head
        while node.pointer is not None and i < index - 1:
            node = node.pointer
            i += 1
        if node.pointer is None:
            return False
        node.pointer = node.pointer.pointer
        if node.pointer is None:  # Removed tail
            self.tail = node
        return True

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.pointer
        return values
