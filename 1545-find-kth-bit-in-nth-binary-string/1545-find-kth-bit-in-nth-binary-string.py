class Solution:
      def findKthBit(self, n: int, k: int) -> str:            
            if n == 1:
                return '0'
            l = int(2 ** n - 1)
            mid = l // 2
            
            if k <= mid:
                return self.findKthBit(n-1,k)
            elif k == mid + 1:
                return '1'
            else:
                k = l - k + 1
                res = self.findKthBit(n-1,k)
                print(f'res {res}')
                return '0' if res != "0" else '1'
#         L = 2**n - 1
#         inv = 0
#         while (n > 1):
#             l = (L - 1) / 2
#             if (k == l + 1):
#                 return '1' if inv % 2 == 0 else '0' # from added 1 in the middle
#             if (k > l + 1):
#                 k -= l + 1
#                 k = l + 1 - k # rev
#                 inv += 1
            
#             L = l
#             n -= 1
        
#         return '0' if inv % 2 == 0 else '1' # from the original 0
#     def findKthBit(self, n: int, k: int) -> str:
        
#         def invert(s:str) -> str:
#             o = ""
#             for item in s:
#                 if item == "0":
#                     o += '1'
#                 else:
#                     o += '0'
#             return o
#         output = [''] * n;
        
#         output[0] = '0'
#         print(output)
#         for i in range(1,n):
#             output[i] = output[i-1] + "1" + invert(output[i-1])[::-1]
        
#         return output[n-1][k-1]
        
