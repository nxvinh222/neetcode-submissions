# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def visit(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False

            return visit(node.left, left, node.val) and visit(node.right, node.val, right)

        return visit(root, -3000000000, 3000000000)
        