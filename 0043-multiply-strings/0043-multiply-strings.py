class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1,num2]:
            return '0'
        num1,num2 = num1[::-1],num2[::-1]
        m,n = len(num1),len(num2)
        res = [0] * (m+n)
        for i in range(m):
            for j in range(n):
                digit = int(num1[i]) * int(num2[j])
                res[i+j] += digit
                res[i+j+1] += (res[i+j]//10)
                res[i+j] = res[i+j] % 10
                
        res,beg = res[::-1],0
        
        while beg < len(res) and res[beg] == 0:
            beg += 1
            
        return "".join(str(x) for x in res[beg:] )