class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_range = min(k,len(nums1))
        heap = [(i + nums2[0],[i,nums2[0]],0) for i in nums1[:min_range]]
        heapq.heapify(heap)
        result = []
        while k > 0 and heap:
            summ,pair,index = heapq.heappop(heap)
            result.append(pair)
            if index + 1 < len(nums2):
                heapq.heappush(
                    heap,(pair[0] + nums2[index+1],[pair[0],nums2[index+1]],index+1)
                )
            k -= 1
        return result
        