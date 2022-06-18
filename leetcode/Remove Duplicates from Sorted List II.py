# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


# Time: O(n) | Space: O(1)
def deleteDuplicates(head):
    sentinel = ListNode(next=head)
    curr, behind = head, sentinel
    while curr:
        if curr.next and curr.next.val == curr.val:
            duplicate = curr.val
            while curr and curr.val == duplicate:
                curr = curr.next
            behind.next = curr
        else:
            curr = curr.next
            behind = behind.next

    head = sentinel.next
    return head


list = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3)))))

print(deleteDuplicates(list))
