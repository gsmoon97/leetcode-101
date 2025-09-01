# 0141 · Linked List Cycle

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | hash-table · linked-list · two-pointers | **Python3** · 51 ms · 39.7 MB | 2025-06-11 20:59 UTC |

---

## Problem Statement
https://leetcode.com/problems/linked-list-cycle

---

## Approach
Floyd’s Tortoise-and-Hare to achieve O(1) space complexity, based on the assumption that if there is a cycle, the fast pointer will eventually 'catch up' with the slow pointer.

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
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 51 ms | 39.7 MB | 19.85 % time · 56.4 % memory | [View](https://leetcode.com/problems/linked-list-cycle/submissions/1661249084/) |
