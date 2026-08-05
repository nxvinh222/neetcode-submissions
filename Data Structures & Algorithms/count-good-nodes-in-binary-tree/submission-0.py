# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def visit(node, prevValue, res):
            if not node:
                return 0
            if node.val >= prevValue:
                res += 1
                prevValue = node.val
            res += visit(node.left, prevValue, 0)
            res += visit(node.right, prevValue, 0)
            return res

        return visit(root, -10001, 0)
        