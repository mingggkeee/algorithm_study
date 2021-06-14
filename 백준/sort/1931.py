def solution(InputArr):
    answer = 0
    endTime = 0
    for i in range(len(InputArr)):
        if endTime <= InputArr[i][0]:
            endTime = InputArr[i][1]
            answer += 1
    return answer

N = int(input())
InputArr = []

for i in range(N):
    num1, num2 = map(int, input().split())
    InputArr.append([num1, num2])
    
InputArr.sort(key=lambda x: (x[1], x[0]))
print(solution(InputArr))