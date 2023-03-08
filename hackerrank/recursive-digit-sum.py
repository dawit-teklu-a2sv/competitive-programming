def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return int(n)
    d_sum = k * sum([int(i) for i in n])
    return superDigit(str(d_sum),1)
