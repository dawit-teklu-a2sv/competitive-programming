class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for item in nums:
            newAnswer = answer[:]
            for ans in newAnswer:
                answer.append(ans + [item])
        return answer