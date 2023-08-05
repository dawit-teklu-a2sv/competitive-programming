class Solution:
    def numberOfPairs(self, A: List[int], B: List[int], diff: int) -> int:
        SHIFT = 30001
        for i in range(len(A)):
            A[i] = A[i] - B[i] + SHIFT
        BIT = [0] * (SHIFT * 2 + 1)
        count = 0
        for j in A:
            count += self.query(BIT, j + diff)
            self.update(BIT, j)
        return count

    def query(self, BIT: List[int], n: int) -> int:
        count = 0
        while n >= 1:
            count += BIT[n]
            n -= (n & -n)
        return count

    def update(self, BIT: List[int], n: int) -> None:
        while n < len(BIT):
            BIT[n] += 1
            n += (n & -n)