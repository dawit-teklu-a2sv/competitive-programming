# Enter your code here. Read input from STDIN. Print output to STDOUT
num_length = int(input())
nums_dict = {}
for i in range(num_length):
    word = input()
    # nums_dict[word] += nums_dict.get(word,0)
    if word in nums_dict:
         nums_dict[word] += 1
    else:
        nums_dict[word] = 1
    
print(len(nums_dict))
print(" ".join(str(x) for x in list(nums_dict.values())))
    
