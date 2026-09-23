# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Valid(node, lo, hi):
            if node is None:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return Valid(node.left, lo, node.val) and Valid(node.right, node.val, hi)
        return Valid(root, float('-inf'), float('inf'))
        