def pushing(c, n):
    if c == ' ':
        return c
    if ord(c) >= 65 and ord(c) <= 96:
        if ord(c) + n <= 96:
            return chr(ord(c) + n)
        else:
            return chr(ord(c) + n - 26)
    elif ord(c) >= 97 and ord(c) <= 122:
        if ord(c) + n <= 122:
            return chr(ord(c) + n)
        else:
            return chr(ord(c) + n - 26)


def solution(s, n):
    answer = ''
    for i in s:
        answer += pushing(i, n)
    return answer

print(solution("asdfsafDFSGrw  dfsfafda DASF", 24))

print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))