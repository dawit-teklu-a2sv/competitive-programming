class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([x for x in range(n,0,-1)])
        
        while len(queue) > 1:
            for  i in range(1,k):
                queue.appendleft(queue.pop())
            queue.pop()
            
        return queue.pop()
            
