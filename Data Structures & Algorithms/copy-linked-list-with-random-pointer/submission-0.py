"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(-1)
        curr = newHead
        mem = {}

        tmpHead = head
        while tmpHead:
            newNode = Node(tmpHead.val)
            mem[tmpHead] = newNode
            tmpHead = tmpHead.next
            curr.next = newNode
            curr = curr.next

        tmpHead = head
        while tmpHead:
            newNode = mem[tmpHead]
            if tmpHead.random:
                newNode.random = mem[tmpHead.random]
            tmpHead = tmpHead.next

        res = newHead.next
        return res
        