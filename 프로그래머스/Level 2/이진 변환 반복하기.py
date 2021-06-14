def solution(s):
    answer = []
    cnt = 0
    cnt2 = 0
    while True:
        if s == "1":
            break
        cnt2 += s.count("0")
        leng = len(s) - s.count("0")
        s = format(leng, 'b')
        cnt += 1
    answer.append(cnt)
    answer.append(cnt2)
    return answer