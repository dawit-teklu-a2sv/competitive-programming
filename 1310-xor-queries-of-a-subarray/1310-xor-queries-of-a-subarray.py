class Solution:
    def xorQueries(self, arr: List[int], q: List[List[int]]) -> List[int]:
        
        n = len(arr)
        prefix = [arr[0]] * n
        
        for i in range(1,n):
            prefix[i] = prefix[i-1] ^ arr[i]
            
        res = []
        
        for item in q:
            R = item[1]
            L = item[0]
            if L == 0:
                res.append(prefix[R])
            else:
                res.append(prefix[R] ^ prefix[L-1])
        return res