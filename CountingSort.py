def countingSort(arr):
    # Write your code here
    # output = [0 for x in range(len(arr))]
    n = len(arr)
    output = [0] * 100
    for i,a in enumerate(arr):
        if output[a] != 0:
            output[a] += 1
        else:
            output[a] = 1
    return output
