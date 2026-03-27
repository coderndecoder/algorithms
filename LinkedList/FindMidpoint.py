# Find and return middle node. If two middle nodes then return the second one.

# Singly list.

from LinkedList import LinkedList, Node
from LinkedListOperations import LinkedListOperations

class FindMidpoint:
    def find_midpoint_node(ll : LinkedList) -> Node:
        slow = fast = ll.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
if __name__ == "__main__":
    
    ll = LinkedList([100,200,300,400,500])
    print(ll)
    result = FindMidpoint.find_midpoint_node(ll)
    print(f" FindMidpoint(ll) for odd nodes # : {result.value}")
    n = LinkedListOperations.insert_node(ll, 600, len(ll))
    print(ll)
    result = FindMidpoint.find_midpoint_node(ll)
    print(f" FindMidpoint(ll) for even nodes # : {result.value}")