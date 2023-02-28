class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.stream = []
        self.equalValues = 0
        

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num == self.value:
            self.equalValues += 1
        if len(self.stream) > self.k:
            temp = self.stream.pop(0)
            if temp == self.value:
                self.equalValues -= 1
        return self.equalValues >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)