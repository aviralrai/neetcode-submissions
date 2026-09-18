# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []
        c = 0
        while curr:
            c += 1
            arr.append(curr)
            curr = curr.next
        for i,node in enumerate(arr):
            nex = arr[c-i-1]
            if nex.next == node.next:
                nex.next = None
                return
            else: nex.next = node.next
            if node.next == nex:
                nex.next = None
                return
            else: node.next = arr[c-i-1]