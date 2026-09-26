# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        prev = None
        head = list1
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev = curr1 
                curr1 = curr1.next
            else:
                if prev is None:
                    head = curr2
                    prev = curr2
                    nex = curr2.next
                    curr2.next = curr1
                    curr2 = nex

                else:
                    prev.next = curr2
                    prev = curr2
                    nex2 = curr2.next
                    curr2.next = curr1
                    curr2 = nex2
        if curr2:
            prev.next = curr2
        return head

        