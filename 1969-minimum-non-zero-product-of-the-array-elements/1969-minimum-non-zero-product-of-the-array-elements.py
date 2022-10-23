class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        max_ = 2 ** p - 1
        return (max_ * (pow(max_ - 1,  (max_ -1 ) //2 , 10 ** 9 + 7))) % (10 ** 9 + 7)
        