class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next


def build_linked_list(nums):
    dummy = ListNode(0)
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

def print_linked_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals

