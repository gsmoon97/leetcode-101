class LRUCache:
    # A simpler Node class to hold the key-value pair and pointers.
    # Storing the key in the node is crucial for eviction.
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}  # The hash map {key: Node}

        # Dummy head and tail nodes to make add/remove operations easier.
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- Helper Methods for Doubly Linked List ---

    def _remove(self, node: Node):
        """Removes a node from its current position in the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        """Adds a node to the end of the list (right before the tail)."""
        # The node before the tail is the current MRU.
        prev_mru = self.tail.prev
        
        # Wire up the new node
        prev_mru.next = node
        node.prev = prev_mru
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        value = -1
        if key in self.key_to_node:
            node = self.key_to_node[key]  # take out node
            value = node.val
            # move the node to end of the list to indicate MRU
            self._remove(node)
            self._add(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:  # if key is already in cache
            node = self.key_to_node[key]
            node.val = value  # update the value
            # move the node to end of the list to indicate MRU
            self._remove(node)
            self._add(node)
            return

        new_node = self.Node(key, value)
        self.key_to_node[key] = new_node
        self._add(new_node)

        if len(self.key_to_node) > self.capacity:  # if cache is full
            lru_node = self.head.next
            self._remove(lru_node)
            del self.key_to_node[lru_node.key]




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)