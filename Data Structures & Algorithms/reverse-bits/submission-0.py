class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # make room, drop in n's last bit
            n >>= 1                            # move to n's next bit
        return result
