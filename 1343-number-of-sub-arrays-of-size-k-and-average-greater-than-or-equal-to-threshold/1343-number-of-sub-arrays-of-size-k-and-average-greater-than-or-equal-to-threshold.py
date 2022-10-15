class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i,j = 0, k
        total = sum(arr[:k])
        output = 1 if total / k >= threshold else 0
        while j < len(arr):
            total += (arr[j] - arr[i])
            if total/ k >= threshold:
                output += 1
            j += 1
            i += 1
        return output