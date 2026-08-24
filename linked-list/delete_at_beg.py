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

head = node1

# Delete from beginning
if head is not None:
    head = head.next

# Display
current = head

while current:
    print(current.data, end=" -> ")
    current = current.next

print("None")