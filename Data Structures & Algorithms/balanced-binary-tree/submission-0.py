# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True
        def calcDepth(root):
            nonlocal bal
            if root is None or bal == False:
                return 0
            l, r = 0, 0
            if root.left: l = calcDepth(root.left)
            if root.right: r = calcDepth(root.right)
            if abs(l - r) > 1:
                bal = False
            return 1 + max(l,r)
        calcDepth(root)
        return bal
        