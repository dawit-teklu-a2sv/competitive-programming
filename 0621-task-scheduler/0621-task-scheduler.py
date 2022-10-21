class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each task takes 1 unit time
        #minmize idle time
        #O(m * n) where m is size of tasks and n is idle time
        
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        q = deque() #includes [count, time]
        time = 0
        heapq.heapify(maxHeap)
        while q or  maxHeap:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
            
        