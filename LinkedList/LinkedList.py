# LinkedList 
from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def __init__(self, arr: List[int]):
        self.head = Node(arr[0])
        curr = self.head
        self.size = len(arr)
        
        for i in range(1, self.size):
            l = Node(arr[i]) 
            curr.next = l
            curr = l
    
    def __str__(self):
        if not self.head:
            print("Linked List is Empty")
            return None
        node = self.head    
        result = ""
        
        while node:
            result += f"{node.value} "
            node = node.next
        return result
    
    def __len__(self):
        return self.size
