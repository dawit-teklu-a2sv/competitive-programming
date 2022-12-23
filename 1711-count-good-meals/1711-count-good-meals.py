class Solution:
 def countPairs(self, deliciousness):
        """
        Given numbers are in range of 0 and 2^20.
        Max sum must be under 2^21 (reason: 2^20 +2^20 = 2^21)
        """
        # O(22N)
        # pre computing powers of 2 for saving time
        powers_of_2 = [2**i for i in range(22)]
        
        # for every number check if its power_of_2 - itself exists
        
        c = Counter() # to keep track of frequency
        ans = 0
        for d in deliciousness:
            # doing this before incremeting value count
            # because we dont want to do increments twice.
            # example in (1,3) there is only one way
            # but we want to the find the way when the pointer is at 3
            # and not at 1.
            for pw in powers_of_2:
                ans += c[pw-d]
            # increment value frequency
            c[d] += 1
        # return result
        return ans % ((10**9) + 7)