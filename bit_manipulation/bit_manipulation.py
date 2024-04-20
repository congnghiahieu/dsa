class Solution:
    def set_bit(self, x: int, position_by_idx: int):
        mask = 0b0000_0001 << position_by_idx
        return x | mask

    def clear_bit(self, x: int, position_by_idx: int):
        mask = 0b0000_0001 << position_by_idx
        return x & ~mask

    def flip_bit(self, x: int, position_by_idx: int):
        mask = 0b0000_0001 << position_by_idx
        return x ^ mask

    def is_bit_set(self, x: int, position_by_idx: int):
        shifted = x >> position_by_idx
        return shifted & 1
