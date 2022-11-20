class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        length1 = len(s1)
        length2 = len(s2)
        arr1 = [0] * 26
        arr2 = [0] * 26
        for i in range(length1):
            arr1[ord(s1[i])-ord('a')] += 1
            arr2[ord(s2[i])-ord('a')] += 1
            
        for j in range(length1,length2):
            if arr1 == arr2:
                return True
            arr2[ord(s2[j-length1])-ord('a')] -= 1
            arr2[ord(s2[j])-ord('a')] += 1
            
        return True if arr1== arr2 else False
            
            

            

            