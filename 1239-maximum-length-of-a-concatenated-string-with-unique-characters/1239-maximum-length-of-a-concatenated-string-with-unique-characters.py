class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isValid(curr,newItem):
            temp = [0] * 26
            for c in newItem:
                temp[ord(c)-ord('a')] += 1
                if temp[ord(c)-ord('a')] > 1 or c in curr:
                    return False
            return True
        
        def backtrack(arr,curr,start):
            nonlocal max_len
            if max_len < len(curr):
                max_len = len(curr)
            for i in range(start,len(arr)):
                if not isValid(curr,arr[i]):
                    continue
                backtrack(arr,curr + arr[i],i+1) 
        max_len = 0
        backtrack(arr,"",0)
        return max_len
            
            
