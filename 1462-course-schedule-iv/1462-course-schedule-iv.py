class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        for u,v in prerequisites:
            indegrees[v] += 1
            graph[u].append(v)
            
        q = deque()
        
        for index,degree in enumerate(indegrees):
            if degree == 0:
                q.append(index)
                
        lookup = {i:set() for i in range(numCourses)}
        
        while q:
            u = q.popleft()
            
            for v in graph[u]:
                lookup[v].add(u)
                lookup[v].update(lookup[u])
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        ans = []
        
        for query in queries:
            ans.append(query[0] in lookup[query[1]])
        return ans
            