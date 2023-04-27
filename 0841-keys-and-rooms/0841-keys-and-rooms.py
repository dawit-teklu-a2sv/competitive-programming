class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque()
        queue.append(0)
        visited = set([0])
        while queue:
            front = queue.popleft()
            
            for room in rooms[front]:
                if room not in visited:
                    visited.add(room)
                    queue.append(room)
        return len(rooms) == len(visited)

        
        