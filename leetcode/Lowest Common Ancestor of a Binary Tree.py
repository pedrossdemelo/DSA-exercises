# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr):
        n = len(arr)
        root = cls(arr[0])
        queue = deque([root])
        i = 1
        while queue and i < n:
            curr = queue.popleft()
            if i < n and arr[i] != None:
                left = cls(arr[i])
                curr.left = left
                queue.append(left)
            i += 1
            if i < n and arr[i] != None:
                right = cls(arr[i])
                curr.right = right
                queue.append(right)
            i += 1
        return root

    def __repr__(s):
        if s == None:
            return ""
        if s.left == s.right == None:
            return str(s.val)
        ans = str(s.val)
        if s.left != None:
            ans = ans + "(" + str(s.left) + ")"
        else:
            ans = ans + "()"
        if s.right != None:
            ans = ans + "(" + str(s.right) + ")"
        return ans

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    visited = set()
    pathp = pathq = None
    def dfs(node, depth=0):
        nonlocal pathp, pathq, visited
        if not node: return
        if node == p:
            pathp = visited.copy()
            return
        if node == q:
            pathq = visited.copy()
            return
        visited.add((depth, node))
        dfs(node.right, depth+1)
        dfs(node.left, depth+1)
        visited.remove((depth, node))
    dfs(root)
    if not pathp:
        return q
    if not pathq:
        return p
    return max(pathp & pathq)[1]

root = TreeNode.from_list([1,2])

print(lowestCommonAncestor(root, root, root.left))
