# LinkedList 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def printList(node: Node):
    while node is not None:
        print(node.value, end=" ")
        node = node.next
    print("\n")
        
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

def replace_node(node: Node, old_value, new_value):
    print("Replacing ", old_value)
    while node:
        if node.value == old_value:
            node.value = new_value
        node = node.next
        
def insert_node(node: Node, value, index) -> Node:
    temp = node
    print("Inserting ", value)
    for i in range(index-1):
        node = node.next
    
    t = node.next
    node.next = Node(value)    
    node.next.next = t
    
    return temp
    

def remove_node(node: Node, value) -> Node:
    temp = node
    print("Removing ", value)
    # first node
    if node.value == value:
        node = node.next
        temp = node
        
    while node:
        if node.next and node.next.value == value:
            node.next = node.next.next       
        node = node.next
        
    return temp


# Test the methods on list        

head = create_a_list([1,2,3,4,1,5,1])
print("List: ")
printList(head)     

# Replace particular number
replace_node(head, 1, 9)
printList(head)

# Insert number at specific index
head = insert_node(head, 8, 1)
printList(head)

# # Remove number from list
head = remove_node(head, 9)
printList(head)




