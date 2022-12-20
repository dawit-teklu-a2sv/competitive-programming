n = int(input())
rooms = list(map(int,input().split()))
family_count = {}
for room in rooms:
    if room in family_count:
        family_count[room] += 1
    else:
        family_count[room] = 1
for room,count in family_count.items():
    if count < n:
        print(room)
        break
