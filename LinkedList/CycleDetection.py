# Determine if LinkedList contains a cycle.

# Conditions: non-unique values, singly linked list

# Two approaches with different space complexity:
# 1. Maintain history of visited nodes with time complexity of O(n) and space O(n)
# 2. Floyd's Cycle Detection algo using fast/slow pointers with time O(n) and space O(1)

from LinkedList import Node, LinkedList
from LinkedListOperations import LinkedListOperations

class CycleDetection:
    def find_cycle_using_visited_nodes_history(head :Node) -> bool:
        node = head 
        visited_nodes = set()
        while node:
            if node in visited_nodes:
                return True
            
            visited_nodes.add(node)
            node = node.next
            
        return False
    
    def find_cycle_floyds_method(head :Node):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
            
if __name__ == "__main__":

    ll = LinkedList([100,200,300,400,500])
    n = LinkedListOperations.insert_node(ll, 600, len(ll))
    
    result = CycleDetection.find_cycle_using_visited_nodes_history(ll.head)
    print(f"find_cycle_using_visited_nodes_history() when no cycle: {result}")
    result = CycleDetection.find_cycle_floyds_method(ll.head)
    print(f"find_cycle_floyds_method() when no cycle: {result}")
    
    # 600 connects to 300 to form cycle
    n.next = ll.head.next.next
    result = CycleDetection.find_cycle_using_visited_nodes_history(ll.head)
    print(f"find_cycle_using_visited_nodes_history() when cycle: {result}")    
    result = CycleDetection.find_cycle_floyds_method(ll.head)
    print(f"find_cycle_floyds_method() when cycle: {result}")  
