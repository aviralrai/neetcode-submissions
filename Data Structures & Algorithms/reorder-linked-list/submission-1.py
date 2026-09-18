# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, f = head, head
        while f and f.next:
            f = f.next.next
            print(curr.val)
            curr = curr.next
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        l = head
        r = prev

        while r.next:
            nex = l.next
            prev = r.next
            r.next = l.next
            l.next = r
            l = nex
            r = prev
        return
