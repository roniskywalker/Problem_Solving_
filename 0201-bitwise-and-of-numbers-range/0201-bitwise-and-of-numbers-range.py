class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        return -1<<(l^r).bit_length()&l