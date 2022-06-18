# https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

# Time: O(n) | Space: O(1)
def swapPairs(head):
    if not head or not head.next:
        return head
    sentinel = ListNode(next=head)
    before, one, two = sentinel, head, head.next
    while two:
        temp = two.next
        before.next = two
        two.next = one
        one.next = temp
        # prepare the next swap
        before = one
        one = temp
        try:
            two = temp.next
        except AttributeError:
            break

    return sentinel.next

list = ListNode(0, ListNode(1, ListNode(2)))

print(swapPairs(list))
