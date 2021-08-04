# 세로 N, 가로 M
N, M = map(int, input().split())
# 좌표 (A, B), 방향 direction
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
A, B, direction = map(int, input().split())
# 맵 정보
# 0: 육지, 1: 바다

# 방문한 위치 저장
d = [[0] * M for _ in range(N)]
d[A][B] = 1

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

# 방향 정의 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시작
count = 1
turn_time = 0
while True:
    # 왼쪽 회전
    turn_left()
    nx = A + dx[direction]
    ny = B + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우에 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        A = nx
        B = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 다 갈 수 없는 경우
    if turn_time == 4:
        nx = A - dx[direction]
        ny = B - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            A = nx
            B = ny
        else:
            break
        turn_time = 0

print(count)