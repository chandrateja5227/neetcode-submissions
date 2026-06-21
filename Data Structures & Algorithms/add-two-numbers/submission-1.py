# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        
        first = l1
        second = l2
        index = 0
        num1 = 0
        while first:
            val = first.val
            num1 += (val * 10**index)
            first = first.next
            index+=1

        index = 0
        num2 = 0
        while second:
            val = second.val
            num2 += (val * 10**index)
            second = second.next
            index+=1

        
        total = num1+num2
        print(total)
        new_head = ListNode(0)
        if total == 0:
            return new_head
        node = new_head
        while total:
            num = total%10
            total = total//10            
            node.next = ListNode(num)
            node = node.next

        return new_head.next



       

        