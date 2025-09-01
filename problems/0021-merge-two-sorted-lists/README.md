# 0021 · Merge Two Sorted Lists

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | linked-list · recursion | **Python3** · 0 ms · 17.8 MB | 2025-06-04 16:45 UTC |

---

## Problem Statement
https://leetcode.com/problems/merge-two-sorted-lists

---

## Approach
In-place merging with two pointers for each list and one pointer for the merged list

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(m + n) | O(1) |

---

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()  # dummy node to keep track of the head
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        # if one of the lists is empty, link to the head of the other list
        tail.next = list1 or list2
        return dummy.next


```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 17.8 MB | 100.0 % time · 61.17 % memory | [View](https://leetcode.com/problems/merge-two-sorted-lists/submissions/1653918832/) |
