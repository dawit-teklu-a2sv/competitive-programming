class ListNode:
    
    def __init__(self,key=-1,val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.maps = [ListNode() for _ in range(1000)]
        
    def getHash(self,key):
        return key % 1000
    def put(self, key: int, value: int) -> None:
        
        curr = self.maps[self.getHash(key)]
        
        while curr.next:
            
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        curr = self.maps[self.getHash(key)].next 
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next 
            
        return -1

        
    def remove(self, key: int) -> None:
        curr = self.maps[self.getHash(key)]
        
        while curr and curr.next:
            
            if curr.next.key == key:
                curr.next = curr.next.next
                
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)