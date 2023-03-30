class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        n = num
        while n > 0:
            count += 1
            n >>= 1
        temp = (1<<count)-1
        return  num ^ temp
#         output = 0
#         while num > 0:
#             output += (2 ** count) * (0 if num & 1 else 1)
#             count += 1
#             num >>= 1
#         return output
    
    