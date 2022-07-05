# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque


# Time: O(n) | Space: O(w)
def connect(root):
    if not root:
        return root
    queue = deque([(root, 0)])
    prev = (None, -1)
    while queue:
        node, depth = queue.popleft()
        prevnode, prevdepth = prev
        if prevdepth == depth:
            prevnode.next = node
        prev = (node, depth)
        if node.left:
            queue.append((node.left, depth+1))
        if node.right:
            queue.append((node.right, depth+1))
    return root