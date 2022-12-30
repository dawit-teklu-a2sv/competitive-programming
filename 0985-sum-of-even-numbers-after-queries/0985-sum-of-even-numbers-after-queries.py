class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # first  calculate the sum of all even numbers
        # then deduct the current number from the sum of evens
        # after adding the query value check if the new added value is even if it's add it to the sum
        # of evens and append it the output array
        output = []
        evenSum = sum([item for item in nums if item % 2 == 0])
        for value,index in queries:
            if nums[index] % 2 == 0:
                evenSum -= nums[index]
            nums[index] += value
            if nums[index] % 2 == 0:
                evenSum += nums[index]
            output.append(evenSum)
        return output