class Node:
    def __init__(self, val : int = None):
        self.value = val
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
  
    def get(self, index: int) -> int:
        i = 0
        node = self.head
        while(node is not None and i < index):
            node = node.pointer
            i+=1
        if(node is not None):
            return node.value
        else:
            return -1


    def insertHead(self, val: int) -> None:
        node = Node(val)
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            node.pointer = self.head
            self.head = node

        
    def insertTail(self, val: int) -> None:
        node = Node(val)
        if(self.tail is None):
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
        if node.pointer is None:  
            self.tail = node
        return True
     

    def getValues(self) -> List[int]:
        values  = []
        node = self.head
        while(node is not None):
            values.append(node.value)
            node = node.pointer
        return values
        


        
