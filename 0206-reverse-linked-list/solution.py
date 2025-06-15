# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.newhead = None
        def dfs(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node.next:
                self.newhead = node
                return node
            prev = dfs(node.next)
            prev.next = node
            return node
        if head:
            tail = dfs(head)
            tail.next = None
        return self.newhead
