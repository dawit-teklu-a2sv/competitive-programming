class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minIndex = -1
        minDistance = float('inf')
        for index,point in enumerate(points):
            if point[0] == x or point[1] == y:
                temp_distance = abs(x-point[0]) + abs(y-point[1])
                if temp_distance < minDistance:
                    minIndex = index
                    minDistance = temp_distance
        return minIndex

            