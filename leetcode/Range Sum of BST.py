# https://leetcode.com/problems/range-sum-of-bst/submissions/

# Time: O(n) | Space: O(h)
def rangeSumBST(root, low, high):
    stack = [root]
    sum = 0
    while stack:
        curr = stack.pop()
        if low <= curr.val <= high:
            sum += curr.val
        if curr.left and curr.val > low:
            stack.append(curr.left)
        if curr.right and curr.val < high:
            stack.append(curr.right)
    return sum