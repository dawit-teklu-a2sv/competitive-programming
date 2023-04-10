"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
            d = {}
            for e in employees:
                d[e.id] = e
                
            def dfs(e_id):
                e = d[e_id]
                importance = e.importance
                
                s_sum = 0
                
                for s in e.subordinates:
                    s_sum += dfs(s)
                return s_sum + importance
            
            return dfs(id)
           