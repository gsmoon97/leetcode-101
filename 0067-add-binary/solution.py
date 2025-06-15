class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        final_bs = []
        
        while i >= 0 or j >= 0 or carry:  # continue until no digits to process and no carry
            total = carry
            # use parity bit (i.e., & 1) to determine if the current digit is 1 or 0
            if i >= 0:
                total += (ord(a[i]) & 1)  # `ord` is marginally faster in converting string to int
                i -= 1
            if j >= 0:
                total += (ord(b[j]) & 1)  # `ord` is marginally faster in converting string to int
                j -= 1

            final_bs.append('1' if total & 1 else '0')  # use parity bit
            carry = total >> 1  # right shift total to get how much to carry over to next operation

        return ''.join(reversed(final_bs))
