# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Time: O(n) | Space: O(n)
def findTarget(root, k):
    inorder = []
    stack, curr = [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        inorder.append(curr.val)
        curr = curr.right
    left, right = 0, len(inorder) - 1
    while left < right:
        sum = inorder[left] + inorder[right]
        if sum == k:
            return True
        elif sum < k:
            left += 1
        elif sum > k:
            right -= 1
    return False

# Time: O(n) | Space: O(n)
def findTarget(root, k):
    seen = set()
    stack = [root]
    while stack:
        curr = stack.pop()
        if not curr: continue
        target = k - curr.val
        if target in seen:
            return True
        seen.add(curr.val)
        stack += [curr.right, curr.left]
    return False