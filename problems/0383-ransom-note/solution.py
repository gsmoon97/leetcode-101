class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):  # early termination
            return False
        counter = [0] * 26  # lowercase English letters
        base = ord('a')
        for m in magazine:
            counter[ord(m) - base] += 1
        for r in ransomNote:
            idx = ord(r) - base
            counter[idx] -= 1
            if counter[idx] == -1:
                return False
        return True