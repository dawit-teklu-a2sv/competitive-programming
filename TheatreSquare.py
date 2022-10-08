 
n, m, a = map(int, input().split(' '))
width = m//a
length = n // a
if m % a != 0:
    width += 1
if n % a != 0:
    length += 1
result =  width * length
print(result)
