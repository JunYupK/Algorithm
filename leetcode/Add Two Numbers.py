class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node = l1
        l2_node = l2
        l1_num = []
        l2_num = []
        while l1_node != None:
            l1_num.append(str(l1_node.val))
            l1_node = l1_node.next
        while l2_node != None:
            l2_num.append(str(l2_node.val))
            l2_node = l2_node.next
        l1_num = int("".join(l1_num[::-1]))
        l2_num = int("".join(l2_num[::-1]))
        answer = list(str(l1_num + l2_num))
        answer = answer[::-1]
        result = tmp_node = ListNode()
        for n in answer:
            n = int(n)
            tmp_node.next = ListNode(n)
            tmp_node = tmp_node.next
        return result.next