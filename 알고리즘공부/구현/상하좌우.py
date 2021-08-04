# 공간의 크기 받기
N = int(input())
# 이동 계획서 받기
commands = list(input().split())

X = 1
Y = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
for command in commands:
    for i in range(len(move_types)):
        if command == move_types[i]:
            nx = X + dx[i]
            ny = Y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

print(X, Y)