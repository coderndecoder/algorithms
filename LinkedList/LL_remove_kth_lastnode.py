# Return the head of a singly Linked List after removing the Kth node from end of it.

# 1. find the Kth node
# 2. remove the Kth node 
# To remove Kth node we need to be at the previous node

from LinkedList import LinkedList, Node

def remove_next_node(node :Node):
    temp = node.next
    node.next = node.next.next
    temp.next = None
    
def remove_kth_last_node(ll :LinkedList, k :int):
    dummy = Node(-1)
    dummy.next = ll.head
    trailer = leader = dummy
    
    # k - leader needs ot be 1 node ahead of Kth node
    for _ in range(k):
        leader = leader.next
        # if k is larger than the len of list
        if not leader:
            return ll.head
        
    # move leader to end of the list along with trailer 
    while leader.next:
        trailer = trailer.next
        leader = leader.next
        
    # Remove the Kth node
    trailer.next = trailer.next.next
    
    return dummy.next


ll = LinkedList([100,200,300,400,500])
print(ll)
k=5
ll.head = remove_kth_last_node(ll, k)
print(f"Removing {k}th node from the end:")
print(ll)