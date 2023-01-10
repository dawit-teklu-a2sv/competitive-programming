class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_indices = []
        for index,item in enumerate(boxes):
            if item == '1':
                one_indices.append(index)
                                    
        output = []
        print(one_indices)
        for i in range(len(boxes)):
            temp_operations  = 0
            for j in one_indices:
                temp_operations += (abs(j-i))
            output.append(temp_operations)
        return output
        