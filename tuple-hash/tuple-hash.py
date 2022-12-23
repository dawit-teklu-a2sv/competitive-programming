#not working in python3 so use pypy 3 language in hackerrank
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()[:n])
    t = tuple(integer_list)
    print(hash(t))
