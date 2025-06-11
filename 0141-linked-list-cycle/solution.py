# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        has_seen = set()  # keep track of all the visited nodes
        node = head
        while node:
            if node in has_seen:
                return True
            has_seen.add(node)
            node = node.next