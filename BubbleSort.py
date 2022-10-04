def countSwaps(a):
    # Write your code here
    count = 0#to track number of swaps
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                count += 1
    print(f'''Array is sorted in {count} swaps.
First Element: {a[0]}
Last Element: {a[len(a) - 1]}''')
