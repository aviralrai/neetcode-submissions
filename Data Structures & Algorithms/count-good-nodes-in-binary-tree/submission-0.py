# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good  = 0
        maxseen = float('-inf')

        def traverse(root, maxseen):
            nonlocal good
            if root is None:
                return
            if root.val >= maxseen:
                good += 1
                maxseen = root.val
            traverse(root.left,maxseen)
            traverse(root.right,maxseen)
            return
        traverse(root, maxseen)
        return good
            

        