class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def maxSum(L:int, M:int) -> int:
            sumL = sumM = 0
            for i in range(0, L + M):
                if i < L:
                    sumL += A[i]
                else:
                    sumM += A[i]    
            maxL, ans = sumL, sumL + sumM
            for i in range(L + M, len(A)):
                sumL += A[i - M] - A[i - L - M]
                maxL = max(maxL, sumL)
                sumM += A[i] - A[i - M]
                ans = max(ans, maxL + sumM)
            return ans
        
        return max(maxSum(L, M), maxSum(M, L))         