def time2min(str):
    h = int(str[0:2])
    m = int(str[3:5])
    h2 = int(str[8:10])
    m2 = int(str[11:13])
    return [h * 60 + m, h2 * 60 + m2]
def minmax(lst1, lst2):
    before = max(lst1[0], lst2[0])
    after = min(lst1[1], lst2[1])
    return [before, after]
def min2time(min1, min2):
    h = "0" + str(min1 // 60)
    if len(h) == 3:
        h = h[1:]
    m = "0" + str(min1 % 60)
    if len(m) == 3:
        m = m[1:]
    h2 = "0" + str(min2 // 60)
    if len(h2) == 3:
        h2 = h2[1:]
    m2 = "0" + str(min2 % 60)
    if len(m2) == 3:
        m2 = m2[1:]

    

    return(h+":" + m + " ~ " + h2+ ":" + m2)
n = int(input())
time_list = []
min_list = []
for i in range(n):
    time_list.append(input())
for i in range(len(time_list)):
    min_list.append(time2min(time_list[i]))
min_list.sort()
temp = min_list[0]
for i in range(n - 1):
    
    temp = minmax(temp, min_list[i + 1])
if temp[0] > temp[1]:
    print(-1)
else:
    print(min2time(temp[0], temp[1]))


