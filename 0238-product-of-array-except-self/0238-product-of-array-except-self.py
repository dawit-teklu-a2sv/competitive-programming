class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_array = []        
        # postfix_array = [1]  * len(nums)
        # output = []
        # product = 1
        # for i in nums:
        #     product *= i
        #     prefix_array.append(product)
        # product = 1
        # for i in range(len(nums)-1,-1,-1):
        #     product *= nums[i]
        #     postfix_array[i] = product
        # for i in range(len(nums)):
        #     if i == 0:
        #         output.append(postfix_array[1])
        #     elif i == len(nums)-1:
        #         output.append(prefix_array[i- 1])
        #     else:
        #         output.append(prefix_array[i-1] * postfix_array[i+1])
        # return output
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
                
        postfix = 1
        for j in range(len(nums) - 1,-1,-1):
            output[j] *= postfix
            postfix *= nums[j]
            
        return output