class Solution:
    def reverse(self,s,i,n):
        if i >= n//2:
            return 
        s[i],s[n-i-1] = s[n-i-1],s[i]
        self.reverse(s,i+1,n)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s,0,len(s))
        