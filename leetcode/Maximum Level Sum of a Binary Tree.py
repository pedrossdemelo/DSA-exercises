# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from collections import deque


# Time: O(n) | Space: O(w)
def maxLevelSum(root):
    queue = deque()
    queue.append(root)
    result = level = 0
    maxsum = float('-inf')
    while queue:
        currsum = 0
        level += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            currsum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if currsum > maxsum:
            maxsum = currsum
            result = level
    return result