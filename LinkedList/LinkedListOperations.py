from LinkedList import LinkedList, Node

class LinkedListOperations:
    
    def replace_node(ll: LinkedList, old_value, new_value):
        print("Replacing ", old_value)
        node = ll.head
        while node:
            if node.value == old_value:
                node.value = new_value
            node = node.next
            
    def insert_node(ll: LinkedList, value, index) -> Node:
        node = ll.head
        print("Inserting ", value)
        for i in range(index-1):
            node = node.next
        
        t = node.next
        n = Node(value) 
        node.next = n   
        node.next.next = t
        
        return n

    def remove_node(ll: LinkedList, value) -> Node:
        node = ll.head
        print("Removing ", value)
        # first node
        if not node:
            return
        # Remove head node
        if node.value == value:
            ll.head = ll.head.next
            node = ll.head
            
        while node:
            if node.next and node.next.value == value:
                node.next = node.next.next       
            node = node.next
            
    def create_a_list(arr)->Node:
        head = Node(arr[0])
        curr = head
        i = 1
        while i < len(arr):
            l = Node(arr[i]) 
            curr.next = l
            curr = l
            i+=1
            
        return head
    
    def printList(node: Node):
        while node is not None:
            print(node.value, end=" ")
            node = node.next
        print("\n")


if __name__ == "__main__":

    # Test the methods on LinkedList class
    ll = LinkedList([1,2,3,4,1,5,1])
    print(ll)


    # Replace particular number
    LinkedListOperations.replace_node(ll, 1, 9)
    print(ll)

    # Insert number at specific index
    LinkedListOperations.insert_node(ll, 8, 1)
    print(ll)

    # Remove number from list
    LinkedListOperations.remove_node(ll, 9)
    print(ll)
