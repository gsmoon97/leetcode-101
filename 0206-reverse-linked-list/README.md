# 0206 · Reverse Linked List

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | linked-list · recursion | **Python3** · 0 ms · 18.8 MB | 2025-06-15 07:51 UTC |

---

## Problem Statement
https://leetcode.com/problems/reverse-linked-list

---

## Approach
Recursion

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(n) |

---

## Code

```python
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

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 18.8 MB | 100.0 % time · 14.67 % memory | [View](https://leetcode.com/problems/reverse-linked-list/submissions/1664710976/) |
