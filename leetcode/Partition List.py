# https://leetcode.com/problems/partition-list/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

# Time: O(n) | Space: O(1)
def partition(head, x):
    gTEx_sentinel = gTEx_tail = ListNode()
    sentinel = ListNode(next=head)
    curr, prev = head, sentinel
    while curr:
        if curr.val >= x:
            prev.next = curr.next
            curr.next = None
            gTEx_tail.next = curr
            gTEx_tail = curr
            curr = prev.next
        else:
            prev = prev.next
            curr = curr.next

    prev.next = gTEx_sentinel.next
    return sentinel.next

list = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

print(partition(list, 3))
