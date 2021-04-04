def solution(new_id):
    x = ''
    new_id.lower()

    for i in new_id:
        if i in ["a", 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w',
         'x', 'y', 'z', '0', '1', '2','3', '4', '5', '6', '7', '8', '9', "-", "_", "."]:
            x = x + i
    while ".." in x:
        x = x.replace("..", ".")

    if x[0] == '.':
        x = x[1:]
    elif x[-1] == '.':
        x = x[:-1]
    if x == '':
        x = 'a'
    if len(x) >= 16:
        x = x[0:15]
    if x[-1] == '.':
        x = x[:-1]
    if len(x) <= 2:
        while len(x) >= 4:
            x += x[-1]
    



    answer = x
    return answer
inp = input()
print(solution(inp))