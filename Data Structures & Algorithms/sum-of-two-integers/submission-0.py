class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF        # keep only the lowest 32 bits
        MAX_INT = 0x7FFFFFFF     # largest positive 32-bit int

        while b != 0:
            carry = ((a & b) << 1) & MASK   # where both bits are 1, carry left
            a = (a ^ b) & MASK              # sum ignoring carries
            b = carry

        # bit 31 set means the 32-bit result is negative; convert back
        return a if a <= MAX_INT else ~(a ^ MASK)