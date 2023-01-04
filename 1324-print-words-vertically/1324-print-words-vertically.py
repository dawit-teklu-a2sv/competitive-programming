class Solution:
    def printVertically(self, s: str) -> List[str]:
        #splitting the input array
        # get the longest item's length and initialize the output 2d array based on the longest length        temp_array = s.split()
        # transpose the 2d array join them and append to the output array
        #time complexity O(n Xm)
        # space complexity O(n)
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

            
            
        
        
    
            