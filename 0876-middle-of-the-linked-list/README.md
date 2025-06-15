# 0876 · Middle of the Linked List

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | linked-list · two-pointers | **Python3** · 0 ms · 17.9 MB | 2025-06-15 11:50 UTC |

---

## Problem Statement
https://leetcode.com/problems/middle-of-the-linked-list/description/

---

## Approach
Use two pointers (`slow` and `fast`); move `slow` by 1 step and `fast` by 2 steps; when `fast` reaches the end, `slow` will be at the middle node (second middle in even-length lists).

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 17.9 MB | 100.0 % time · 8.0 % memory | [View](https://leetcode.com/problems/middle-of-the-linked-list/submissions/1664892551/) |
