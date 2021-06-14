def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            answer.append(i)
    for i in range(len(answer)//2+1):
        if (answer[i]+2) * (answer[-i-1]+2) - yellow == brown:
            return [answer[-i-1]+2, answer[i]+2]