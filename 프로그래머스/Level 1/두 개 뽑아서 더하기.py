def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if i == k:
                continue
            else:
                answer.append(numbers[i]+numbers[k])
            
    answer = sorted(list(set(answer)))
    return answer