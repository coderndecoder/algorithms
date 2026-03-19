from LinkedList import LinkedList, Node

class LLReversal:
    
    def iterative(self, ll :LinkedList):
        
        curr_node, prev_node = ll.head, None
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        ll.head = prev_node
        
    def recursive(self, node :Node):
        
        if not node.next:
            return node
        
        new_head = self.recursive(node.next) 
        node.next.next = node
        node.next = None
        
        return new_head
                  
        
    
    
 # Create a LinkedList to reverse
ll = LinkedList([100,200,300,400,500])
print("Original List:")
print(ll)

# Iterative Way
LLReversal().iterative(ll)
print("Iterative reversed List:")
print(ll)

# Recursive Way
ll.head = LLReversal().recursive(ll.head)
print("Recursive reversed List:")
print(ll)

    