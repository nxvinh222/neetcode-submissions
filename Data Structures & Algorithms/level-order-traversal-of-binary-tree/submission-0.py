# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeStack = deque()
        nodeStack.append(root)
        res = []
        nodesThisLevel = 1
        nodesArrayThisLevel = []

        while len(nodeStack) > 0:
            for _ in range (len(nodeStack)):
                node = nodeStack.popleft()
                if node:
                    nodesArrayThisLevel.append(node.val)
                    nodeStack.append(node.left)
                    nodeStack.append(node.right)

            if bool(nodesArrayThisLevel):
                res.append(nodesArrayThisLevel)
            nodesArrayThisLevel = []

        return res
        