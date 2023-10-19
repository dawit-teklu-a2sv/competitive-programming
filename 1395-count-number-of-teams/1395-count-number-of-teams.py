class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        length = len(rating)
        
        left_array = [0] * length
        right_array = [0] * length
        
        for i in range(length):
            count = 0
            for j in range(i):
                if rating[i] > rating[j]:
                    count += 1
            left_array[i] = count 
            
        for j in range(length-1,-1,-1):
            count = 0
            for i in range(length-1,j,-1):
                if rating[j] > rating[i]:
                    count += 1
            right_array[j] = count
            
        res = 0
        
        for i in range(length):
            
            for j in range(i):
                if rating[i] > rating[j]:
                    res += left_array[j]
        for j in range(length-1,-1,-1):
            for i in range(length-1,j,-1):
                if rating[j] > rating[i]:
                    res += right_array[i]
                    
        return res
                    

        
#         count = 0
        
#         for i in range(len(rating)):
#             for j in range(i+1,len(rating)):
#                 for k in range(j+1,len(rating)):
#                     if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
#                         count += 1
                        
#         return count
            
            
        