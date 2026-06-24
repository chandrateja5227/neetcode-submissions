# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        node = lists[0]
        for i in range(1,len(lists)):
            node = self.merge(node,lists[i])
            print(node.val)

        return node

    def merge(self,list1 , list2):
        first = ListNode(0,list1)
        right = ListNode(0,list2)
        result = first
        while first.next and right.next:

            if first.next.val <= right.next.val:
                first = first.next
            else:
                first.next = ListNode(right.next.val,first.next)
                first = first.next
                right = right.next

        while right.next:
            first.next = ListNode(right.next.val,first.next)
            first = first.next
            right = right.next

        return result.next










        