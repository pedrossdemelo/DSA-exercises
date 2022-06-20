# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        if self == None:
            return ""
        if self.left == self.right == None:
            return str(self.val)
        ans = str(self.val)
        if self.left != None:
            ans = ans + "(" + str(self.left) + ")"
        else:
            ans = ans + "()"
        if self.right != None:
            ans = ans + "(" + str(self.right) + ")"
        return ans


def createPBT(l):
    ptrs = [None] * len(l)
    for i, v in enumerate(l):
        lefti, righti = ((i + 1) * 2) - 1, (i + 1) * 2
        if lefti >= len(l): continue
        leftv, rightv = l[lefti], l[righti]
        if not ptrs[i]:
            n = Node(v)
            left, right = Node(leftv), Node(rightv)
            n.left, n.right = left, right
            ptrs[i], ptrs[lefti], ptrs[righti] = n, left, right
        else:
            left, right = Node(leftv), Node(rightv)
            ptrs[i].left, ptrs[i].right = left, right
            ptrs[lefti], ptrs[righti] = left, right
    return ptrs[0]

tree = createPBT([1,2,3,4,5,6,7])

# Time: O(n) | Space: O(n)
def connect(root: "Optional[Node]") -> "Optional[Node]":
    q = deque([root])
    prev, i, next_layer = None, 1, 2
    while q:
        curr = q.popleft()
        if curr.right:
            q.append(curr.left)
            q.append(curr.right)
        if i == next_layer:
            next_layer *= 2
            prev = None
        if prev: prev.next = curr
        prev = curr
        i += 1
    return root

print(connect(tree))

