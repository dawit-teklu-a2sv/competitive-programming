class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        #KMP Approach
        m = len(needle)
        lps = [0] * m 
        i,j = 0,1
        while  j < m:
            if needle[i] == needle[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = lps[i-1]
                    
        j,i = 0,0
        print(lps)
        while j < len(haystack):
            if i == m - 1 and needle[i] == haystack[j]:
                return j - i
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = lps[i-1]
      
        return -1
        #Rabin Carp Algorith
        a = 27
        mod = 10 ** 9 + 7
        n_length = len(needle)
        
        def getHash(word):
            hash = 0
            k = len(word) - 1 
            for ch in word:
                hash += (a ** k) * (ord(ch)-ord('a')+1)
                k -= 1
            return hash % mod
        def addLast(current_hash,ch):
            
            return (current_hash * a + (ord(ch)-ord('a') + 1)) % mod
        
        def pollFirst(current_hash,ch):
            return ((current_hash)  - (a**(n_length-1) * (ord(ch)-ord('a') + 1 )))%mod
            
        
        n_hash = getHash(needle)
        hay_hash = getHash(haystack[:n_length])
        left  = 0

        if n_hash == hay_hash:
            return 0
        for i in range(n_length,len(haystack)):
            if n_hash == hay_hash:
                return i - n_length
            hay_hash = pollFirst(hay_hash,haystack[i-n_length])
            hay_hash = addLast(hay_hash,haystack[i])
            
        #Naive Approach
        if hay_hash == n_hash:
            return len(haystack) - n_length
        return -1
                

        for i in range(len(haystack)):
            temp = i 
            count = 0
            for j in range(len(needle)):
                if temp < len(haystack):
                    if haystack[temp] == needle[j]:
                        temp += 1 
                        count += 1
                    else:
                        break 
            else:
                if count == len(needle):
                    ans = min(ans,i)
                
        return ans if ans != float('inf') else -1
        