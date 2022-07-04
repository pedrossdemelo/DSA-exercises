# https://leetcode.com/problems/balanced-binary-tree/submissions/

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


# Time: O(n) | Space: O(1)
def isBalanced(root):
    result = True
    def dfs(node, depth=0):
        nonlocal result
        if result == False:
            return
        if not node:
            return depth
        maxdepthleft = dfs(node.left, depth+1)
        maxdepthright = dfs(node.right, depth+1)
        if abs(maxdepthleft - maxdepthright) > 1:
            result = False
            return
        return max(maxdepthleft, maxdepthright)
    dfs(root)
    return result

root = TreeNode.from_list([3,9,20,None,None,15,7])
print(isBalanced(root))
