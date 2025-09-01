# 0208 · Implement Trie (Prefix Tree)

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | hash-table · string · design · trie | **Python3** · 39 ms · 32.1 MB | 2025-09-01 21:24 UTC |

---

## Problem Statement
https://leetcode.com/problems/implement-trie-prefix-tree/

---

## Approach
Implement `TrieNode` class to construct `Trie`: `TrieNode` class has two attributes: 1) children (a dictionary where key is the character and value is the `TrieNode` object of the child) 2) is_terminal (a boolean to indicate whether the current node is terminal i.e., end of the word)

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(m) | O(m x n) |

---

## Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 39 ms | 32.1 MB | 80.81 % time · 75.65 % memory | [View](https://leetcode.com/problems/implement-trie-prefix-tree/submissions/1756366335/) |
