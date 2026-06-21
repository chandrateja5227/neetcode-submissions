# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        count = 0

        while node:
            count += 1
            node = node.next
        curr = head
        prev = None
        for i in range(count):
            if i == (count-n):
                if prev:
                    prev.next = curr.next if curr.next  else None
                    return head
                else:
                    curr = curr.next 
                    return curr
            prev = curr
            curr = curr.next if curr else None
            

        return head

            


        
        