def arrayManipulation(n, queries):
   # Write your code here
    nums = defaultdict(int)
    
    for start, end, value in queries:
       nums[start] += value
       nums[end + 1] -= value 
       
    pref_sum = [item for index,item in sorted(nums.items())]
    
    n = len(pref_sum)
    for i in range(1,n):
        pref_sum[i] += pref_sum[i-1]
    return max(pref_sum)
