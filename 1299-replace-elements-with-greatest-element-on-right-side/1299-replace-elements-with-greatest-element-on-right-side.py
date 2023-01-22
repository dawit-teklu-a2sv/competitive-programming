class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = arr[-1]
        output = []
        for i in range(len(arr)-1,-1,-1):
            output.append(current_max)
            if current_max < arr[i]:
                current_max = arr[i]
        start = 0
        end = len(output) - 1
        while start < end:
            output[start],output[end] = output[end],output[start]
            start += 1
            end -= 1
        output[-1] = -1
        return output
        