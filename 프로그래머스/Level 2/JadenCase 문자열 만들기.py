def solution(s):
    s = s.lower()
    split = s.split(" ")
    answer = ''
    for i in split:
        i = i.capitalize()
        answer += i+" "
    return answer[:-1]