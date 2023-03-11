class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        
        for i in range(k):
            current_sum += nums[i]
        max_sum = current_sum
        
        left = 0
        for i in range(k,len(nums)):
            current_sum = current_sum + nums[i] - nums[left]
            left += 1
            max_sum = max(max_sum,current_sum)
        return max_sum / k
    
        ## brute force approach 
        
#         max_sum = sum(nums[0:k])
        
#         for i in range(len(nums) - k + 1):
#             current_sum = 0
#             for j in range(i,i + k):
#                 current_sum += nums[j]
#             max_sum = max(max_sum,current_sum)
#         return max_sum / k
                
            
        