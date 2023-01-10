class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k 
        self.lastEqualValues = 0
        self.stream = []
        
    def consec(self, num: int) -> bool:

        self.stream.append(num)
        if num == self.value:
            self.lastEqualValues += 1        
        if len(self.stream) > self.k:
            item = self.stream.pop(0)
            if item == self.value:
                self.lastEqualValues -= 1
        return self.lastEqualValues == self.k
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)