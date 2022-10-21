class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k 
        self.deque = [0] * k
        self.front,self.rear = 0,0
        self.size = 0
        

    def insertFront(self, val: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.deque[self.front] = val
        else:
            self.front = self.front - 1 % self.k
            self.deque[self.front] = val
        self.size += 1
        return True

    def insertLast(self, val: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.deque[self.rear] = val
        else:
            self.rear = self.rear + 1 % self.k 
            self.deque[self.rear] = val
        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = self.front + 1 % self.k 
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.rear = self.rear - 1 % self.k 
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True
    def getFront(self) -> int:
        return self.deque[self.front] if not self.isEmpty() else - 1

    def getRear(self) -> int:
        return self.deque[self.rear] if not self.isEmpty() else - 1

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.k == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()