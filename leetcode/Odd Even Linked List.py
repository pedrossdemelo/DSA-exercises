# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val, self.next = val, next

    def __repr__(self) -> str:
        try:
            return f"{self.val} -> {self.next}"
        except RecursionError:
            return "∞"

# Time: O(n) | Space: O(1)
def addEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(next=head)
    odds_sentinel = odds_tail = ListNode()
    prev = sentinel
    i = 1
    while prev.next:
        curr = prev.next
        if i % 2 == 0:
            prev.next = prev.next.next
            curr.next = None
            odds_tail.next = curr
            odds_tail = curr
        else:
            prev = prev.next
        i += 1
    prev.next = odds_sentinel.next
    return sentinel.next

def llfroml(l):
    head = None
    while l: head = ListNode(l.pop(), head)
    return head

print(addEvenList(llfroml([2,1,3,5,6,4,7])))
