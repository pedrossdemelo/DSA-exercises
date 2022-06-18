# https://leetcode.com/problems/rotate-list/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

# Time: O(n) | Space: O(1)
def rotateRight(head, k):
    if not head: return
    sentinel = ListNode(next=head)
    slow = fast = head
    prev_slow = sentinel
    len = 0
    # get length of the linked list, and also the middle node and the node
    # before the middle
    while fast:
        len += 2
        prev_slow = prev_slow.next
        slow = slow.next
        try:
            fast = fast.next.next
        except AttributeError:
            len -= 1
            break
    slow_i = (len + 1) // 2
    # if we're shifting more than the number of nodes, reduce it to the mod
    k %= len
    # skip if no rotations
    if k == 0: return head
    # since we cant shift right on a singly linked list, we're shifting left
    # with len - k rotations
    k = len - k
    i, prev, curr = 0, sentinel, head
    # if the slow_i (the middle) is smaller than k, shift it already to the
    # middle
    if slow_i <= k:
        i, prev, curr = slow_i, prev_slow, slow
    while i < k:
        i += 1
        prev, curr = prev.next, curr.next
    prev.next = None
    sentinel.next = curr
    while curr.next:
        curr = curr.next
    curr.next = head
    return sentinel.next

list = None

print(rotateRight(list, 3))