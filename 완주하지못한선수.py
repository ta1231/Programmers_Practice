# 답은 맞았으나 효율성에서 틀림
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(zip(participant, completion))
for i in completion:
    if i in participant:
        del(participant[participant.index(i)])
print(participant[0])

def solution(s, c):
    s.sort()
    c.sort()
    # print(zip(s, c))
    for par, com in zip(s, c):
        if par != com:
            return par  #설명 1

    return s[-1]  #설명 2

# 설명 1 동명이인이 있다면, zip 안에 있는 값이 다른 것이 있기 때문에 그 다른 것들 중 하나가 답이 되거나
# 설명 2 zip안에 짝지어진 값이 모두 같거나, 중복된 것이 맨 뒤에 정렬됐다면 길이가 하나 차이 나는 s의 마지막 값이 답이 된다.
