# 0206 · Reverse Linked List

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | linked-list · recursion | **Python3** · 0 ms · 18.5 MB | 2025-06-15 08:01 UTC |

---

## Problem Statement
https://leetcode.com/problems/reverse-linked-list

---

## Approach
Iteration with two persistent pointers `prv` (previous node) and `cur` (current node). Since only one link is reversed per iteration, two pointers that respectively point to the source and destination of the link are sufficient.

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv, cur = None, head
        while cur:
            nxt = cur.next  # temporarily save where to iterate next
            cur.next = prv  # reverse the link (from prv -> cur to cur -> prv)
            prv, cur = cur, nxt  # update the pointers for next iteration
        return prv
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 18.5 MB | 100.0 % time · 95.87 % memory | [View](https://leetcode.com/problems/reverse-linked-list/submissions/1664719385/) |
