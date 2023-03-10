class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(array,start):
            if len(array) == k:
                answer.append(array.copy())
                return
                
            for i in range(start,n+1):
                array.append(i)
                backtrack(array,i+1)
                array.pop()
        backtrack([],1)
        return answer
                