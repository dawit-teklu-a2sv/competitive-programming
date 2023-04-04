class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # count = 0
        # while x > 0 and y > 0:
        #     if x & 1 != y & 1:
        #         count += 1
        #     x >>= 1
        #     y >>= 1
        # while x > 0:
        #     if x & 1 == 
        #     1:
        #         count += 1
        #     x >>= 1
        # while y > 0:
        #     if y & 1 == 1:
        #         count += 1
        #     y >>= 1
        # return count
        # return floor(log2(x ^ y))
        temp = x ^ y
        count = 0
        while temp > 0:
            if temp & 1:
                count += 1
            temp >>= 1
        return count
        
            
        