def solution(n, lost, reserve):
    answer = n - len(lost)
    inter = []
    for i in reserve:
        if i in lost:
            inter.append(i)
    for i in inter:
        reserve.remove(i)
        lost.remove(i)    
    answer += len(inter)

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
            answer += 1
            continue
        elif i + 1 in lost:
            lost.remove(i + 1)
            answer += 1
            continue
    return answer

print(solution(5, [2, 3, 4], [3, 4, 5]))