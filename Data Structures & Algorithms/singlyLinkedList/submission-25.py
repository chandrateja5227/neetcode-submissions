class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
          
    def get(self, index: int) -> int:
        node = self.head
        i = 0
        while node:
            if i == index:
                return node.value
            i+=1
            node = node.next
        return -1



      
    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        

    def insertTail(self, val: int) -> None:
        node = Node(val)
        temp = self.head
        if temp is None:
            self.head = node
            return       
        while temp.next:
            temp = temp.next
        temp.next = node
                 

    def remove(self, index: int) -> bool:
        node = self.head
        i = 0
        if node is None:
            return False
        if index == i:
            self.head = self.head.next
            return True
        while node.next is not None and i < index:
            if i == index - 1:
                node.next = node.next.next
                return True
            node = node.next
            i += 1
        return False





        
    def getValues(self) -> List[int]:
        node = self.head
        list = []
        while node is not None:
            list.append(node.value)
            node = node.next

        return list



        
