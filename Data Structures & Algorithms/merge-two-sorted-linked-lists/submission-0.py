# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        if not list1:
            return list2
        
        if not list2:
            return list1

        if list1.val < list2.val:
            res = ListNode(list1.val)
            list1 = list1.next
        else:
            res = ListNode(list2.val)
            list2 = list2.next

        curr = res
        while list1 or list2:
            if not list1:
                curr.next = list2
                break
            if not list2:
                curr.next = list1
                break
            
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next

        return res
        