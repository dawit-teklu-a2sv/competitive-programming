# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
students_subscribed_english = set(input().split()[:n])
b = int(input())
students_subscribed_french = set(input().split()[:b])
at_least_one_newspaper_subscribed = students_subscribed_english.difference(students_subscribed_french)
print(len(at_least_one_newspaper_subscribed))
