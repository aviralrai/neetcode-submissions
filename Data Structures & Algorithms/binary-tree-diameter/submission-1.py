# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def traverse(root) -> int:
            nonlocal ans
            if root is None:
                return 0
            d_l = traverse(root.left)
            d_r = traverse(root.right)
            ans = max(ans, d_l+d_r)
            return 1 + max(d_l,d_r)
        depth = traverse(root)
        return ans
        