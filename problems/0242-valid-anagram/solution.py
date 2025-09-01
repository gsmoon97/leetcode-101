class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # early termination when mismatch in length
            return False
        counter = [0] * 26  # 26 since the characters consist of lowercase English letters
        base = ord('a')
        for char_s, char_t in zip(s, t):
            counter[ord(char_s) - base] += 1  # increment count for s
            counter[ord(char_t) - base] -= 1  # decrement count for t
        return all(c == 0 for c in counter)  # check that all the post-processed counts are 0