# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        arr = []

        def visit(node):
            if not node:
                return

            visit(node.left)
            arr.append(node.val)
            visit(node.right)

        visit(root)

        return arr[k - 1]
        