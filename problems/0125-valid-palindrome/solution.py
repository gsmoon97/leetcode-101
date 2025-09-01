class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # convert all uppercases to lowercases
        left = 0
        right = len(s) - 1
        while left < right:
            left_c = s[left]
            if not left_c.isalnum():  # skip if not alphanumeric
                left += 1
                continue
            right_c = s[right]
            if not right_c.isalnum():  # skip if not alphanumeric
                right -= 1
                continue
            if left_c != right_c:
                return False
            left += 1
            right -= 1
        return True