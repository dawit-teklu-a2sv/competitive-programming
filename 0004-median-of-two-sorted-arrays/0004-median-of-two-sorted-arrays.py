class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left,right = 0,0
        output = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                output.append(nums1[left])
                left += 1
            elif nums1[left] > nums2[right]:
                output.append(nums2[right])
                right += 1
        while left < len(nums1):
            output.append(nums1[left])
            left += 1
        while right < len(nums2):
            output.append(nums2[right])
            right += 1
        length = len(output)
        if length % 2 == 0:
            return (output[length//2 - 1] + output[length//2]) / 2
        else:
            return output[length//2]
#         nums1_length = len(nums1)        
#         nums2_length = len(nums2)

#         nums1_mid =  (nums1_length and nums1[nums1_length//2 - 1] + nums1[nums1_length//2])/2 if  nums1_length % 2 == 0  else nums1[nums1_length//2]
#         nums2_mid =  (nums2_length and nums2[nums2_length//2 - 1] + nums2[nums2_length//2])/2 if nums2_length % 2 == 0  else nums2[nums2_length//2]
#         return (nums1_mid + nums2_mid) /2 
            
        