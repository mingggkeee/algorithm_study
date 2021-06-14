def solution(array, commands):
    answer = []
    for command in commands:
        arr1 = array[command[0]-1:command[1]]
        arr1.sort()
        answer.append(arr1[command[2]-1])
    return answer