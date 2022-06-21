# https://leetcode.com/problems/design-circular-queue/


class DLLNode:
    def __init__(self, val=0, prev=None, next=None) -> None:
        self.val, self.prev, self.next = val, prev, next

    def __repr__(self) -> str:
        try:
            prev = "" if self.prev else "None <- "
            next = f" <-> {self.next}" if self.next else " -> None"
            return prev + f"{self.val}" + next
        except RecursionError:
            return "∞"


class MyCircularQueue:
    def __init__(self, k: int):
        self.cap, self.len = k, 0
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.head = self.tail = DLLNode(value)
        else:
            self.tail.next = DLLNode(value, self.tail)
            self.tail = self.tail.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.len == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
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
