# 0721 · Accounts Merge

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · string · depth-first-search · breadth-first-search · union-find | **Python3** · 38 ms · 20.9 MB | 2025-09-08 21:32 UTC |

---

## Problem Statement
https://leetcode.com/problems/accounts-merge/

---

## Approach
Union-Find: 1) Each element (e.g., email) starts as its own group. 2) Union: Merge any two elements that belong to the same group (e.g., two different emails under the same account). 3) Find: Find all elements (e.g., emails) that belong in the same group (e.g., same account)

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n log n) (dominated by sorting of emails for each account; Union-Find operations are considered as O(1)) | O(n) |

---

## Code

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union-find approach
        # transitive merging (if a -> b and b -> c, then a -> c)
        # path compression
        
        parent = {}  # key: email, value: parent email
        email_to_name = {}  # to keep track of which name the email belongs to
        def find_root(email):
            if parent[email] != email:
                parent[email] = find_root(parent[email])
            return parent[email]

        def union(email1, email2):
            parent[find_root(email2)] = find_root(email1)

        # initialize union find
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)  # point all emails in the account to the first email of the account
        
        # group emails by root
        groups = defaultdict(set)
        for email in parent:
            groups[find_root(email)].add(email)

        # build result
        result = []
        for root, emails in groups.items():
            name = email_to_name[root]  # find the corresponding name using the root
            account = [name] + sorted(emails)  # concatenate all the emails in sorted order
            result.append(account)
        return result
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 38 ms | 20.9 MB | 35.52 % time · 62.85 % memory | [View](https://leetcode.com/problems/accounts-merge/submissions/1764302362/) |
