month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

def solution(a, b):
    date = 0
    for i in range(a):
        date += month[i]
    date += b
    answer = week[(date + 4) % 7]
    return answer

print(solution(5, 24))