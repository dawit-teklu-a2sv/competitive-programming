def insertionSort1(n, arr):
    # Write your code here
    last_element = arr[n-1]
    for i in range(n-1,0,-1):
        if last_element < arr[i-1]:
            arr[i] = arr[i-1]
        else:
            arr[i] = last_element
        print(*arr,sep=' ')
