def solution(lottos, win_nums):
    cnt = 0
    zerocnt = 0
    for i in lottos:
        if i == 0:
            zerocnt += 1
        elif i in win_nums:
            cnt += 1
        else:
            pass
        
    a = 7 -cnt -zerocnt
    b = 7 -cnt
    if a == 7:
        a = 6
    if b == 7:
        b = 6
    answer = [a, b]
    return answer