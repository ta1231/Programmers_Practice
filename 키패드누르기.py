def get_distance(a, b):
    location = {"1": (1, 1), "2": (1, 2), "3": (1, 3),
                "4": (2, 1), "5": (2, 2), "6": (2, 3),
                "7": (3, 1), "8": (3, 2), "9": (3, 3),
                "*": (4, 1), "0": (4, 2), "#": (4, 3)}
    return abs(location[a][0] - location[b][0]) + abs(location[a][1] - location[b][1])


def solution(numbers, hand):
    answer = ""
    Lhand = "*"
    Rhand = "#"
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            Lhand = str(i)
        elif i in [3, 6, 9]:
            answer += "R"
            Rhand = str(i)
        else:
            if get_distance(Lhand, str(i)) == get_distance(Rhand, str(i)):
                if hand == "right":
                    answer += "R"
                    Rhand = str(i)
                else:
                    answer += "L"
                    Lhand = str(i)
            elif get_distance(Lhand, str(i)) > get_distance(Rhand, str(i)):
                answer += "R"
                Rhand = str(i)
            else:
                answer += "L"
                Lhand = str(i)
                
            
    return answer