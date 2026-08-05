"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if len(node.neighbors) == 0:
            return Node(node.val)

        memo = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None

            if node.val in memo:
                return memo[node.val]

            res = Node(node.val)
            memo[res.val] = res
            for neighbor in node.neighbors:
                newNode = dfs(neighbor)
                res.neighbors.append(newNode)

            memo[res.val] = res
            return res

        return dfs(node)
        