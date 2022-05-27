class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head ,n):
        current_node = head
        count = 1
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        if count <= 1:
            return None
        current_node = head
        for i in range((count - n) - 1):
            current_node = current_node.next

        if count - n == 0:
            return head.next
        current_node.next = current_node.next.next
        return head

