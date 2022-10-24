class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s:str) -> str:
            o = ""
            for item in s:
                if item == "0":
                    o += '1'
                else:
                    o += '0'
            return o
        output = [''] * n;
        
        output[0] = '0'
        print(output)
        for i in range(1,n):
            output[i] = output[i-1] + "1" + invert(output[i-1])[::-1]
        
        return output[n-1][k-1]
        
