# https://leetcode.com/problems/count-complete-tree-nodes/

from collections import deque
from math import log
from time import process_time_ns


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

# Time: O((logn)**2) | Space: O(logn)
def countNodes(root):
    if not root:
        return 0
    if not root.left:
        return 1
    curr, height = root, 1

    while curr.left:
        curr = curr.left
        height += 1

    minnodes = 2 ** (height - 1) - 1
    above_floor_row, floor_row = 2 ** (height - 2), 0

    lo, hi = 0, above_floor_row - 1
    iterations = 0

    def dig(target, node=root, pos=hi / 2, step=above_floor_row / 4):
        nonlocal iterations
        iterations += 1
        if pos == target:
            return node
        elif pos > target:
            return dig(target, node.left, pos - step, step / 2)
        elif pos < target:
            return dig(target, node.right, pos + step, step / 2)

    while lo <= hi:
        iterations += 1
        mid = (lo + hi) // 2
        above_floor_node = dig(mid)
        if not above_floor_node.left:
            hi = mid - 1
        elif above_floor_node.right:
            lo = mid + 1
        else:
            floor_row = mid * 2 + 1
            break

    if not floor_row:
        floor_row = lo * 2
    nodes = minnodes + floor_row

    print(f"Iterations: {iterations} | Time Complexity: {log(nodes, 2) ** 2}")
    return nodes

def countNodes(root):
    def depth(root):
        depth = -1
        while root:
            root = root.left
            depth += 1
        return depth
    nodes = 0
    currdepth = depth(root)
    while root:
        if depth(root.right) == currdepth - 1:
            nodes += 2 ** currdepth
            root = root.right
        else:
            nodes += 2 ** (currdepth - 1)
            root = root.left
        currdepth -= 1
    return nodes


tempstart = process_time_ns()
array = list(range(1_000_000))
root = TreeNode.from_list(array)
tempend = process_time_ns()
elapsed = tempend - tempstart
print(f"Creation of Perfect Binary Tree: {elapsed} nanoseconds ({elapsed/10**9} seconds)")

tempstart = process_time_ns()
print(countNodes(root))
tempend = process_time_ns()
elapsed = tempend - tempstart
print(f"Counting of nodes: {elapsed} nanoseconds ({elapsed/10**9} seconds)")
