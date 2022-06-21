# https://leetcode.com/problems/design-circular-queue/


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val, self.next = val, next

    def __repr__(self) -> str:
        try:
            return f"{self.val} -> {self.next}"
        except RecursionError:
            return "∞"


class MyCircularQueue:
    def __init__(self, k: int):
        self.cap, self.len = k, 0
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.head = self.tail = ListNode(value)
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.len == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.cap == self.len
