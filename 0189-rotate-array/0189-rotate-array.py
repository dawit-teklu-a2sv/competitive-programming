class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # if k == 0 or k == len(nums) we need not to do nothing.
        def flip(start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        flip(0,len(nums)-1)
        flip(0,k-1)
        flip(k,len(nums)-1)