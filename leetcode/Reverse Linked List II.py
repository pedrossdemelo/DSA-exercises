# https://leetcode.com/problems/reverse-linked-list-ii/


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

# Time O(n) | Space: O(1)
def reverseBetween(head, left, right):
    sentinel = ListNode(next=head)
    curr = sentinel
    i = 0
    while i < left - 1:
        curr = curr.next
        i += 1
    l_join = curr
    curr = curr.next
    reverse_tail = curr
    prev = None
    while i < right:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        i += 1
    l_join.next = prev
    reverse_tail.next = curr
    return sentinel.next


list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(reverseBetween(list, 2, 4))
