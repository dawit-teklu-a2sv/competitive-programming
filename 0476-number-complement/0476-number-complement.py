class Solution:
    def findComplement(self, num: int) -> int:
        length = num.bit_length()
        mask = (1 << length) - 1
        return num ^ mask
        # n = num
        # n |= n >> 1
        # n |= n >> 2
        # n |= n >> 4
        # n |= n >> 8
        # n |= n >> 16
        # return n ^ num
        # temp = num & (num-1)
        # if temp == 0:
        #     return num ^ (num * 2 - 1)
        # else:
        #     return num ^ (temp * 2 - 1)
        # mask = (num & (num - 1)) * 2 - 1
        # if mask < 0:
        #     return 0
        # return mask ^ num
        # count = 0
        # n = num
        # while n > 0:
        #     count += 1
        #     n >>= 1
        # temp = (1<<count)-1
        # return  num ^ temp
#         output = 0
#         while num > 0:
#             output += (2 ** count) * (0 if num & 1 else 1)
#             count += 1
#             num >>= 1
#         return output
    
    