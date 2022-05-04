"""
使用Doubly Linked List来存储LRU，而且使用两个特殊的Node来表示前后
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # cache： key => node
        self.cache = {}
        # 虚拟节点不在cache里面
        self.left = Node(0, "left")
        self.right = Node(0, "right")
        # left和right要先连上
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """
        Remove the LRU from ANY place in the list.
        """
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.cache.pop(node.key)

    def insert(self, node):
        """
        Insert to prev of self.right.
        """
        prev = self.right.prev
        # 互相建立联系
        prev.next, node.prev = node, prev
        node.next, self.right.prev = self.right, node
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 把node从原来的位置删掉，再放到self.right的prev去
        if node.next == self.right:
            return node.value
        else:
            self.remove(node)
            self.insert(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        # 需要提前判断一下，cache里面有没有key，如果有需要删掉
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        self.insert(Node(key, value))
        if len(self.cache) > self.cap:
            # 此时需要remove
            self.remove(self.left.next)
        assert len(self.cache) <= self.cap


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def test_solution():
    """
    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
    """
    # ex. 1
    input1 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    input2 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expect1 = [None, None, None, 1, None, -1, None, -1, 3, 4]
    # ex. 2
    input3 = ["LRUCache", "put", "put", "put", "put", "get", "get"]
    input4 = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    expect2 = [None, None, None, None, None, -1, 3]
    examples = [
        (input3, input4, expect2),    
        (input1, input2, expect1), 
    ]
    for input1, input2, expect in examples:
        instance = None
        for n, (input_1, input_2, expect_1) in enumerate(zip(input1, input2, expect)):

            def init(*cap):
                nonlocal instance
                instance = LRUCache(*cap)

            func = {
                "LRUCache": init,
                "put": LRUCache.put,
                "get": LRUCache.get,
            }[input_1]
            if instance:
                res = func(instance, *input_2)
            else:
                res = func(*input_2)
            if expect_1:
                assert res == expect_1, (n, input_1, input_2, expect_1, res)
