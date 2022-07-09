# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Time: O(height + k) | Space: O(height)
def kthSmallest(root, k):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k-=1
        if k == 0:
            return curr.val
        curr = curr.right