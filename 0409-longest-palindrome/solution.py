class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = [0] * (26 * 2)  # 2 sets (upper and lower) of 26 alphabets
        base_A = ord('A')
        base_a = ord('a')
        for c in s:
            offset = ord(c) - base_A
            if offset > 25:
                offset = ord(c) - base_a + 26
            counter[offset] += 1
        
        has_odd_count = False
        len_pal = 0
        for count in counter:
            if (count % 2) != 0:
                has_odd_count = True
            len_pal += (count // 2) * 2
        return (len_pal + 1) if has_odd_count else len_pal

        
