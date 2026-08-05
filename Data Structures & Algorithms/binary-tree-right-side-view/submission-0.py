# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        nodeArrayThisLevel = deque()
        nodeArrayThisLevel.append(root)
        length = 1

        while length != 0:
            for i in range(length):
                node = nodeArrayThisLevel.popleft()
                if i == length - 1:
                    res.append(node.val)
                if node.left:
                    nodeArrayThisLevel.append(node.left)
                if node.right:
                    nodeArrayThisLevel.append(node.right)

            length = len(nodeArrayThisLevel)

        return res
        