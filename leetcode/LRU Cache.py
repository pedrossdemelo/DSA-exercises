# https://leetcode.com/problems/lru-cache/

class DLLNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

    def __str__(self):
        return f"({self.key}: {self.val}) <-> {self.next}"

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        if capacity == 1:
            return
        self.len = 2
        self.most_recent = DLLNode(0,0)
        self.least_recent = DLLNode(0,0)
        self.most_recent.prev = self.least_recent
        self.least_recent.next = self.most_recent

    def del_lru(self):
        self.len -= 1
        lrukey = self.least_recent.key
        self.least_recent = self.least_recent.next
        self.least_recent.prev = None
        if lrukey in self.cache:
            del self.cache[lrukey]

    def upgrade(self, node):
        if node == self.most_recent:
            return
        elif node == self.least_recent:
            self.least_recent = self.least_recent.next
            self.least_recent.prev = None
            node.prev = node.next = None
            self.len -= 1
            self.insert(node)
        else:
            self.extract(node)
            self.insert(node)

    def insert(self, node):
        if self.len + 1 > self.cap:
            self.del_lru()
        self.len += 1
        self.most_recent.next = node
        node.prev = self.most_recent
        self.most_recent = node
        if node.key not in self.cache:
            self.cache[node.key] = node

    def extract(self, node):
        prev, next = node.prev, node.next
        node.prev.next = next
        node.next.prev = prev
        node.next = node.prev = None
        self.len -= 1

    def get(self, key: int) -> int:
        if self.cap == 1:
            if key in self.cache:
                return self.cache[key]
            else:
                return -1
        if key in self.cache:
            self.upgrade(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 1:
            if key in self.cache:
                self.cache[key] = value
            else:
                self.cache.clear()
                self.cache[key] = value
            return
        if key in self.cache:
            self.upgrade(self.cache[key])
            self.cache[key].val = value
        else:
            node = DLLNode(key, value)
            self.insert(node)

LRU = LRUCache(1)

LRU.put(2, 1)

LRU.get(2)

LRU.put(3, 2)

LRU.get(2)

LRU.get(3)

LRU.put(4,2)
