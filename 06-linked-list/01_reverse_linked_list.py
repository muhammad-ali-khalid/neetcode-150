# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        next_node = None
        while head:
            new_node = ListNode(head.val, next_node)
            next_node = new_node
            head = head.next
        return new_node