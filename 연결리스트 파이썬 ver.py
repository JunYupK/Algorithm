class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_node(node):
    while node != None:
        print(node.data)
        node = node.next
def add_node(head, data):
    curr_node = head
    new_node = Node(data)
    while curr_node.next != None:
        curr_node = curr_node.next
    curr_node.next = new_node
def remove_node(head, target):
    prev_node = head
    curr_node = head.next
    while curr_node.data != target:
        prev_node = curr_node
        curr_node = curr_node.next
    prev_node.next = curr_node.next

Head = Node(0)
for i in range(1,11):
    add_node(Head,i)
remove_node(Head,9)
print_node(Head)
