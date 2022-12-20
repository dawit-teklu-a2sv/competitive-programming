# Enter your code here. Read input from STDIN. Print output to STDOUT

def isValidCube(cubes):
    left,right = 0,len(cubes) - 1
    prev = float('inf')
    while left < right:
        if cubes[left] >= cubes[right] and cubes[left] <= prev:
            prev = cubes[left]
            left += 1
        elif cubes[right] >= cubes[left] and cubes[right] <= prev:
            prev = cubes[right]
            right -= 1
        else:
            return "No"
    return "Yes"
    
T = int(input())
for i in range(T):
    length = int(input())
    arrays = list(map(int,input().split()))[:length]
    res = isValidCube(arrays)
    print(res)
