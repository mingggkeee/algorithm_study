def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                cnt += 1
                answer.append(cnt)
                cnt = 0
                break
            else:
                cnt +=1
        if cnt != 0:
            answer.append(cnt)
    answer.append(0)
    return answer