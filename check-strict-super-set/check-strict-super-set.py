# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_super_set(super_test,test_set):
    if len(test_set) >= len(super_test):
        return False
    for item in test_set:
        if item not in super_test:
            return False 
    return True

A = set(input().split())
count = int(input())
isSuperSet = True
for i in range(count):
    sub_set = set(input().split()) 
    if not is_super_set(A,sub_set):
        isSuperSet = False
        break 
print(isSuperSet)

