class Solution:
    def __init__(self):
        self.previous_values = {}
    def fib(self, n: int) -> int:
        if n in self.previous_values:
            return self.previous_values[n]
        if n <= 1:
            return n
        self.previous_values[n] = self.fib(n-1) + self.fib(n-2)
        return self.previous_values[n]
        