class MapSum:

    def __init__(self):
        self.map = {}
        self.score = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        temp = val - self.map.get(key,0)
        self.map[key] = val
        for i in range(1,len(key) + 1):
            pref = key[:i]
            self.score[pref] += temp
        print("score",self.score)

    def sum(self, prefix: str) -> int:
        return self.score[prefix]
        


        
        
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)