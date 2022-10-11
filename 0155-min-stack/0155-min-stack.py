class MinStack:

    def __init__(self):
        self.stack = []
        self.minArrays = []
        

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val)
            self.minArrays.append(min(val,self.minArrays[-1]) )
        else:
            self.stack.append(val)
            self.minArrays.append(val)

    def pop(self) -> None:
            self.stack.pop()
            self.minArrays.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minArrays:
            return self.minArrays[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()