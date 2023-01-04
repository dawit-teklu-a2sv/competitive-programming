class Solution:
    def printVertically(self, s: str) -> List[str]:
        # temp_array = s.split() #holds string s after spliting 
        # longest_length = len(temp_array[0]) #marks the length of the output array to be returned
        # index = -float('inf')
        # for i in range(1,len(temp_array)):
        #     if len(temp_array[i]) > longest_length:
        #         longest_length = len(temp_array[i])
        #         index = i
        # output = [''] * longest_length # output array
        # for item in temp_array:
        #     for i in range(len(item)):
        #         output[i] += item[i]
        # print(output
        # if index != -float('inf'):
        #     output[len(output)-1] = f"{'' * index}{temp_array[index][-1]}"
        # print(output)
        temp_array = s.split()
        longest_len = len(temp_array[0])
        for item in temp_array:
            if len(item) > longest_len:
                longest_len = len(item)
        matrix = [[' ' for _ in range(len(temp_array))] for _ in range(longest_len)]
        for i in range(len(temp_array)):
            for j,value in enumerate(temp_array[i]):
                    matrix[j][i] = value
        output = []
        for item in matrix:
            j = "".join(item).rstrip()
            output.append(j)
        return output

            
            
        
        
    
            