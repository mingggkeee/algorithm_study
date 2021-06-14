def solution(d, budget):
    answer = 0
    buds = 0
    d.sort()
    for i in d:
        if buds <= budget:
            if budget - buds < i:
                break
            else:
                answer += 1
                buds += i
        else:
            break
    return answer