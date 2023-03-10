class Solution:
    def splitString(self, s: str) -> bool:
#         current = []
        
#         def backtrack(index,prev):
#             if len(current) >= 2:
#                 return True
            
#             for i in range(index,len(s)):
#                 val = int(s[index:index+1])
#                 if prev -1 == val or not current:
#                     if backtrack(index + 1, val):
#                         return True
#                     current.pop()
#             return False
#         backtrack()
        def backtrack(prev,index):
            if index == len(s):
                return True
            for j in range(index,len(s)):
                val = int(s[index:j+1])
                if prev-1 == val:
                    if backtrack(val,j+1):
                        return True
            return False
        for i in range(len(s)-1):
            val = int(s[:i+1])
            result =  backtrack(val,i+1)
            if result:
                return True
        return False