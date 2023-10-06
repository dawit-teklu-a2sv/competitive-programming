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
#Using floyd warshal 
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #using floyd warshall algorithm
        courses = [[False]*numCourses for _ in range(numCourses)]
        
        for pre,course in prerequisites:
            courses[pre][course] = True
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    courses[i][j] = courses[i][j] or courses[i][k] and courses[k][j]
        
        output = []
        for pre,course in queries:
            output.append(courses[pre][course])
            
        return output
            
            
    
        
        
    
        
            
