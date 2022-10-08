def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    elevation = 0
    for i in range(steps):
        if path[i] == "U":
            elevation -= 1
        elif path[i] == "D":
            elevation += 1
        if elevation == 0 and path[i] == 'U':
                valleys += 1
    return valleys
