class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def solve(nums,left,right):
            if left == right:
                return nums[left]
            
            left_choice = nums[left] - solve(nums,left+1,right)
            right_choice = nums[right] - solve(nums,left,right-1)
            
            return max(left_choice,right_choice)
        result =  solve(nums,0,len(nums)-1)
        return result >= 0
        
        
        