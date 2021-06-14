def solution(s):
    s = s.upper()
    count1 = 0 ; count2 = 0
    for i in s:
        if i == 'P':
            count1 += 1
        elif i == 'Y':
            count2 += 1
        else:
            pass
        
    if count1 == count2:
        answer = True
    else:
        answer = False
    return answer