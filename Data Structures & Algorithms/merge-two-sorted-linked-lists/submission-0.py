# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1


        left = list1
        right = list2
        s_list = None
        head = None
        while left and right:
            if left.val <= right.val:
                if s_list:
                    s_list.next = ListNode(left.val)
                    s_list = s_list.next                  
                else:
                    s_list = ListNode(left.val)
                    head = s_list
                left = left.next
            else:
                if s_list:
                    s_list.next = ListNode(right.val)
                    s_list = s_list.next 
                else:
                    s_list = ListNode(right.val)
                    head = s_list
                right = right.next
            


        while left:
            if s_list:
                s_list.next = ListNode(left.val)
                s_list = s_list.next 
            left = left.next

        while right:
            if s_list:
                s_list.next = ListNode(right.val)
                s_list = s_list.next 
            right = right.next

        return head


