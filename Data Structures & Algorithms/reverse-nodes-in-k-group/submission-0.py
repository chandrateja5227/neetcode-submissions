# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = ListNode(0,head)
        start = first
        pointer = first
        while True:
            pointer = self.nextKpossible(pointer,k)
            if pointer:
                right = start.next
                
                while start.next != pointer:
                
                    node = start.next
                    start.next = node.next
                    node.next = pointer.next
                    pointer.next = node

                pointer = start = right
            else:
                break
    
                        
        return first.next            
      
    def nextKpossible(self,pointer,k):
        
        for _ in range(k):
            if pointer:
                pointer = pointer.next
            else:
                break 

        return pointer


        



        