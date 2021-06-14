def solution(dartResult):
    temp2 = list(dartResult)
    answer = []
    temp = []
    for i in range(len(temp2)):
        if temp2[i] == '1' and temp2[i+1] == '0':
            temp.append('10')
        elif temp2[i] == '0' and temp2[i-1] == '1':
            continue
        else:
            temp.append(temp2[i])
    
    for i in range(1, len(temp)):
        if temp[i] == 'S':
            answer.append(int(temp[i-1]))
        elif temp[i] == 'D':
            answer.append(int(temp[i-1])**2)
        elif temp[i] == 'T':
            answer.append(int(temp[i-1])**3)
        
        if temp[i] == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif temp[i] == '#':
            answer[-1] = answer[-1] * (-1)
            
    return sum(answer)