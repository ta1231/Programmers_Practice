def solution(n):
    result = 0
    answer = ""
    while n != 0:
        answer = answer + str(n % 3)
        n = n // 3
    
    for i in range(len(answer)):
        result += int(answer[len(answer) - 1 - i]) * (3 ** i)

    return result
print(solution(45))