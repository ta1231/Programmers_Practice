def solution(priorities, location):
    queue = []
    for i, x in enumerate(priorities):
        queue.append((i + 1, x))
    
    while queue:
        idx = queue.index(max(queue, key = lambda x : x[1]))
        print(queue.pop(idx))
        if max(queue, key = lambda x : x[1]) in queue[idx:][:][1]:
            idx = queue.index(max(queue[idx:], key = lambda x : x[1])) + idx
            print(queue.pop(idx))
        else:
            idx = queue.index(max(queue, key = lambda x : x[1]))
            print(queue.pop(idx))
    return 0

solution([1, 1, 9, 1, 1, 1], 0)