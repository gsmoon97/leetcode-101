# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # slow visits one node per iteration
            fast = fast.next.next  # fast visits two nodes per iteration
            if slow is fast:  # if fast catches up with slow, there is a cycle
                return True
        return False  # if fast never catches up with slow and reaches the end, there is no cycle