# Least Recently Used cache:
# LRUCache(capacity: int) - Initiate cache with specificed capacity.
# get(key: int) -> int - Return the value associated with a key. Return -1 if the key doesn't exist.
# put(key: int, value: int) -> None - Add key and value ot the cache. If the addition will result in capacity overflow, remove the least used element. 
#                                       If key already exist, update its value.

# Positive integers
# Capacity is positive

# Solution:
# Data structure - hash map to search keys on O(1) and to implement ordered cache use doubly linkedList
# Head - points to the start head, tail - point to the end of list node

class Doubly_linkedlist_Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_hashmap = {}
        self.head = Doubly_linkedlist_Node(-1,-1)
        self.tail = Doubly_linkedlist_Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def put(self, key: int, value: int):
        if key in self.cache_hashmap:
            self.remove_node(self.cache_hashmap[key])
        
        node = Doubly_linkedlist_Node(key, value)
        self.cache_hashmap[key] = node
        
        if len(self.cache_hashmap) > self.capacity:
            del self.cache_hashmap[self.head.next.key]
            self.remove_node(self.head.next)
        
        self.add_to_tail(node)
            
    def get(self, key :int) -> int:
        
        if key not in self.cache_hashmap:
            return -1
        
        self.remove_node(self.cache_hashmap[key])
        self.add_to_tail(self.cache_hashmap[key])
        return self.cache_hashmap[key].value
        
    def add_to_tail(self, node: Doubly_linkedlist_Node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node 
            
    def remove_node(self, node: Doubly_linkedlist_Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def __str__(self):
        node = self.head.next
        list = ""
        while node != self.tail:
            list += f"{node.value} "
            node = node.next
        return list




lru_cache = LRUCache(3)
lru_cache.put(1, 100)
print("Cache: ", lru_cache)
lru_cache.put(2, 250)
print("Cache: ", lru_cache)
print("get(2):", lru_cache.get(2))
print("Cache: ", lru_cache)
lru_cache.put(4, 300)
print("Cache: ", lru_cache)
lru_cache.put(3, 200)
print("Cache: ", lru_cache)
print("get(4):", lru_cache.get(4))
print("Cache: ", lru_cache)
print("get(1):", lru_cache.get(1))
print("Cache: ", lru_cache)
