# https://leetcode.com/problems/find-mode-in-binary-search-tree/

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

# Time: O(n) | Space: O(1) (without counting call stack)
def findMode(root):
    result = (float('-inf'), [])
    curr, count = None, float('-inf')

    def dfs(node):
        nonlocal curr, count, result
        if not node:
            return
        dfs(node.left)
        if node.val != curr:
            if result[0] < count:
                result = (count, [curr])
            elif result[0] == count:
                result[1].append(curr)
            curr = node.val
            count = 0
        count += 1
        dfs(node.right)
    dfs(root)

    if result[0] < count:
        result = (count, [curr])
    elif result[0] == count:
        result[1].append(curr)

    return result[1]

root = TreeNode.from_list([1,None,2,2])
print(findMode(root))