class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        for item in nums2:
            while stack and stack[-1] < item:
                d[stack.pop()] = item
            stack.append(item)
        for i in range(len(nums1)):
            nums1[i] = d.get(nums1[i],-1)
        return nums1