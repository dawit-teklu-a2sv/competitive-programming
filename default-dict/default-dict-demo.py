from collections import defaultdict
n,m = list(map(int,input().split()))
group_a = [input() for i in range(n)]
group_b = [input() for i in range(m)]
d = defaultdict(list)
for i in range(len(group_a)):
    d[group_a[i]].append(str(i + 1))
    
for item in group_b:
    if item in d:
        print(" ".join(d[item])) 
    else:
        print(-1)   
