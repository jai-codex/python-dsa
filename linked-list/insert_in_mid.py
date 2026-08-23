class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(30)

# Link nodes
node1.next = node2
node2.next = node3

head = node1


# Insert at position
data = 20
position = 2

new_node = Node(data)

current = head

for i in range(position - 1):
    current = current.next

new_node.next = current.next
current.next = new_node


# Display
current = head

while current:
    print(current.data, end=" -> ")
    current = current.next

print("None")