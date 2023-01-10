class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        temp_dict = {}
        for index,item in enumerate(nums):
            temp_dict[item] = index
            
        for num1,num2 in operations:
            temp_dict[num2] = temp_dict[num1]
            del temp_dict[num1]
        result = sorted(temp_dict.items(),key = lambda item:item[1])
        return [x for x,y in result]

        