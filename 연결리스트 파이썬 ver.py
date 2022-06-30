class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def print_node(node):
    while node.next != None:
        print(node.data)
        node = node.next

Head = Node(-1)
prev_node = Head
for i in range(10):
    tmp_node = Node(i)
    prev_node.next = tmp_node
    prev_node = tmp_node

print_node(Head)
print_node(Head)
