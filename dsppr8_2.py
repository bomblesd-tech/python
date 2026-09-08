class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create a node
node = Node(10)

print("Data:", node.data)
print("Previous:", node.prev)
print("Next:", node.next)