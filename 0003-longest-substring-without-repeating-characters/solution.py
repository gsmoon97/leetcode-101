class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_length = 0
        for end, char in enumerate(s):
            if char in seen:
                start = max(seen[char] + 1, start)  # update start to the very next character after the duplicate (but only update if the current start is earlier than the updated start)
            seen[char] = end
            max_length = max(max_length, end - start + 1)  # update the maximum length to keep track of the length of the longest substring
        return max_length