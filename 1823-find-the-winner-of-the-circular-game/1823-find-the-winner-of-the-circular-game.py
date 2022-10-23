class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([x for x in range(n,0,-1)])
        
        while len(queue) > 1:
            i = k 
            while i > 1:
                queue.appendleft(queue.pop())
                i -= 1
            queue.pop()
            
        return queue.pop()
            
