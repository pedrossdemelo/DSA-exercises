# https://leetcode.com/problems/validate-binary-tree-nodes/

from collections import deque

# Time: O(n) | Space: O(n)
def validateBinaryTreeNodes(n, leftChild, rightChild):
    nodesWithoutParent = [*(set(range(n)) - set(leftChild + rightChild))]
    root = nodesWithoutParent[0] if len(nodesWithoutParent) == 1 else None
    if root is None: return False
    queue = deque([root])
    inserted = {root}
    while queue:
        node = queue.popleft()
        left, right = leftChild[node], rightChild[node]
        if left in inserted or right in inserted:
            return False
        if left >= 0:
            inserted.add(left)
            queue.append(left)
        if right >= 0:
            inserted.add(right)
            queue.append(right)
    return len(inserted) == n

args = (
4,
[3,-1,1,-1],
[-1,-1,0,-1]
)
print(validateBinaryTreeNodes(*args))