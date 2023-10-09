class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        ans = float('inf')
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            temp = i 
            count = 0
            for j in range(len(needle)):
                if temp < len(haystack):
                    if haystack[temp] == needle[j]:
                        temp += 1 
                        count += 1
                    else:
                        break 
            else:
                if count == len(needle):
                    ans = min(ans,i)
                
        return ans if ans != float('inf') else -1
        