# https://leetcode.com/problems/longest-univalue-path/

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

# Time: O(n) | Space: O(height of tree)
def longestUnivaluePath(root):
    result = 1
    def dfs(node):
        nonlocal result
        if not node: return None, 0
        val_l, streak_l = dfs(node.left)
        val_r, streak_r = dfs(node.right)
        if val_l != node.val: streak_l = 0
        if val_r != node.val: streak_r = 0
        result = max(result, 1 + streak_l + streak_r)
        return node.val, 1 + max(streak_l, streak_r)
    dfs(root)
    return result - 1

root = TreeNode.from_list([1,4,5,4,4,None,5,9,4,None,None,5,None,None,None,None,4])
print(longestUnivaluePath(root))