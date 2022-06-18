# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

# Time: O(n) | Space: O(1)
def deleteDuplicates(head):
    curr = head
    while curr:
        if curr.next and curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

list = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3)))))

print(deleteDuplicates(list))
