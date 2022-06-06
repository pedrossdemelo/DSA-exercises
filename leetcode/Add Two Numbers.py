# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = num2 = ""
    while l1 or l2:
        num1 = (str(l1.val) if l1 else "") + num1
        num2 = (str(l2.val) if l2 else "") + num2
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    sum = str(int(num1) + int(num2))
    result = None

    for num in sum:
        num = int(num)
        result = ListNode(num, result)

    return result or ListNode(0)


l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))

print(addTwoNumbers(l1, l2))
