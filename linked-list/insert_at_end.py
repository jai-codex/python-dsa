class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(20)
node4 = Node(30)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head
head = node1

# Insert at end
new_node = Node(40)

current = head

while current.next is not None:
    current = current.next

current.next = new_node


# Display
current = head

while current:
    print(current.data, end=" -> ")
    current = current.next

print("None")