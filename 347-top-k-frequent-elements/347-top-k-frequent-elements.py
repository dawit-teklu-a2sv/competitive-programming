class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        result = []
        for i in nums:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1
        output = sorted(output.items(),key=lambda x: -x[1])
        i = 0
        while i < k:
            result.append(output[i][0])
            i += 1
        return result
                         

                
        
        