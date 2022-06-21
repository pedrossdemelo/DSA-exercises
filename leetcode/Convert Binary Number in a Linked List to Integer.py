# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val, self.next = val, next

    def __repr__(self) -> str:
        try:
            return f"{self.val} -> {self.next}"
        except RecursionError:
            return "∞"


def getDecimalValue(head):
    res = 0
    while head:
        res <<= 1
        res += head.val
        head = head.next
    return res


print(getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))))
