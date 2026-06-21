# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next == None:
            return None

        node = head
        stack = []
       
        while node:
            stack.append(node)
            node = node.next
            
        count = len(stack)//2
        curr = head

        for i in range(count):
            last_node = stack.pop()
            temp = curr.next
            curr.next = last_node
            last_node.next = temp
            curr = temp

        curr.next = None



        
        