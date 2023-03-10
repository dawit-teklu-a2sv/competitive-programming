class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # answer = [[]]
        # for item in nums:
        #     newAnswer = answer[:]
        #     for ans in newAnswer:
        #         answer.append(ans + [item])
        # return answer
        answer = []
        def backtrack(array,index,length):
            if index == length:
                answer.append(array)
                return 
            backtrack(array,index + 1,length)
            backtrack(array + [nums[index]],index + 1,length)
        backtrack([],0,len(nums))
        return answer
                