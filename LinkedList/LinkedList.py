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
        size = len(arr)
        
        for i in range(1, size):
            l = Node(arr[i]) 
            curr.next = l
            curr = l
    
    def printList(self):
        if not self.head:
            print("Linked List is Empty")
            return
        node = self.head    
        while node:
            print(node.value, end=" ")
            node = node.next
        print("\n")
