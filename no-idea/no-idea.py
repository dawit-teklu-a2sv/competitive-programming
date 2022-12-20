n,m = input().split()[:2]
arrays = input().split()[:int(n)]
setA = set(input().split()[:int(m)])
setB = set(input().split()[:int(m)])
happiness = 0
for item in arrays:
    if item in setA:
        happiness += 1
    elif item in setB:
        happiness -= 1
        
print(happiness)
