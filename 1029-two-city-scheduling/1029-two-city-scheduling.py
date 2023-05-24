class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        difference = []
        for i,cost in enumerate(costs):
            difference.append([i,cost[0]-cost[1]])
        difference.sort(key=lambda x: x[1])
        totalSum = 0
        for i in range(n//2):
            totalSum += costs[difference[i][0]][0]
        for i in range(n//2,n):
            totalSum += costs[difference[i][0]][1]
        return totalSum
        