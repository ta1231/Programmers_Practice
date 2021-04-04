def solution(priorities, location):
    answer = 0
    from collections import deque

    d = []
    for i, v in enumerate(priorities):
        d.append((v, i))

    while len(d):
        item = d.pop(0)
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer