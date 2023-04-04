class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        
        def backtrack(count,l,index):
            nonlocal ans
            if index == len(requests):
                for item in count:
                    if item:
                        return 
                ans = max(ans,l)
                return 
            #not taking
            backtrack(count,l,index+1)
            #taking
            count[requests[index][0]] -= 1
            count[requests[index][1]] += 1
            backtrack(count,l+1,index+1)
            count[requests[index][0]] += 1
            count[requests[index][1]] -= 1
        count = [0] * n
        backtrack(count,0,0)
        return ans

            