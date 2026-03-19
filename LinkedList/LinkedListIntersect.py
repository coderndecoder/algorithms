# Return the node where two singly linked list intersect, if not then return null.

# Assumptions: Node do not have unique values, once they intersect rest of the list is shared. 
# Two linked list converge at the a shared node

# Solution: Traverse both the list, once they reach the end, traverse the pointer with the other list. 
# They will at a point be on the same shared node 

from LinkedList import LinkedList

def find_LL_intersect(ll1 : LinkedList, ll2 :LinkedList):
    
    nodeA = ll1.head
    nodeB = ll2.head
    
    while nodeA != nodeB:
        
        nodeA = nodeA.next if nodeA else ll2.head
        nodeB = nodeB.next if nodeB else ll1.head
        
    return nodeA

ll1 = LinkedList([100,200,300,400,500,600])
ll2 = LinkedList([100,200])
# Intersect at node 400
ll2.head.next.next = ll1.head.next.next.next

node = find_LL_intersect(ll1,ll2)
print(f"Shared node is {node.value}")
