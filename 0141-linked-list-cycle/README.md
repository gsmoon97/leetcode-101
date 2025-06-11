# 0141 · Linked List Cycle

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | hash-table · linked-list · two-pointers | **Python3** · 55 ms · 16.7 MB | 2025-06-11 20:49 UTC |

---

## Problem Statement
https://leetcode.com/problems/linked-list-cycle

---

## Approach
One-pass iteration of all the nodes while keeping track of all visited nodes in a hash-set

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
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 55 ms | 16.7 MB | 20.37 % time · 5.57 % memory | [View](https://leetcode.com/problems/linked-list-cycle/submissions/1661242785/) |
