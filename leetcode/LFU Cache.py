# https://leetcode.com/problems/lfu-cache/

from collections import namedtuple, OrderedDict

# OrderedDictCount, an OrderedDict with a Count value
ODC = namedtuple("ODC", "count dict")


class ListNode:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data, self.prev, self.next = data, prev, next

    def __repr__(self) -> str:
        try:
            prev = "" if self.prev else "None <- "
            next = f" <-> {self.next}" if self.next else " -> None"
            return prev + f"{self.data}" + next
        except RecursionError:
            return "∞"


class LFUCache:
    def __init__(self, capacity: int):
        self.sentinel = ListNode()
        self.cap = capacity
        self.counts = {}
        self.keys = {}

    def del_node(self, node):
        next, prev = node.next, node.prev
        if next:
            next.prev = prev
        if prev:
            prev.next = next
        del self.counts[node.data.count]

    def insert_node(self, count, key, value, prev, next):
        node = ListNode(ODC(count, OrderedDict([(key, value)])), prev, next)
        if prev:
            prev.next = node
        if next:
            next.prev = node
        self.counts[count] = self.keys[key] = node

    def del_lfu(self):
        head = self.sentinel.next
        lfu_key = head.data.dict.popitem(last=False)[0]
        if len(head.data.dict) == 0:
            self.del_node(head)
        del self.keys[lfu_key]

    def inc_key(self, key, new_value=None):
        oldnode = self.keys[key]
        newcount = oldnode.data.count + 1
        value = oldnode.data.dict[key]
        del oldnode.data.dict[key]
        if new_value:
            value = new_value
        if newcount in self.counts:
            self.counts[newcount].data.dict[key] = value
            self.keys[key] = self.counts[newcount]
        else:
            self.insert_node(newcount, key, value, oldnode, oldnode.next)
        if len(oldnode.data.dict) == 0:
            self.del_node(oldnode)

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        else:
            self.inc_key(key)
            return self.keys[key].data.dict[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.keys:
            if len(self.keys) == self.cap:
                self.del_lfu()
            if 1 not in self.counts:
                self.insert_node(1, key, value, self.sentinel, self.sentinel.next)
            else:
                self.counts[1].data.dict[key] = value
                self.keys[key] = self.counts[1]
        else:
            self.inc_key(key, value)


methods = ["put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
args = [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
expected = [None,None,1,None,-1,3,None,-1,3,4]

cache = LFUCache(2)

for method, arg, expect in zip(methods, args, expected):
    print(f"Calling: {method}({arg})")
    result = getattr(cache, method)(*arg)
    print(f"Got: {result}")
    print(f"Expected: {expect}")
    if result != expect:
        print(f"DISCREPANCY: {result} != {expect}")
