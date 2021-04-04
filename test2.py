def isOk(room, x, y, n):
    for i in range(n):
        for j in range(n):
            if room[x + i][y + j] == "0":
                return 0
    
    return 1


n = int(input())
room = []
lst = [0] * (n + 1)
for i in range(n):
    room.append(input())

for i in range(1, n + 1):
    for x in range(n + 1 - i):
        for y in range(n + 1 - i):
            lst[i] += isOk(room, x, y, i)

print("total: {}".format(sum(lst)))
for i in range(n + 1):
    if lst[i] != 0:
        print("size[{}]: {}".format(i, lst[i]))




