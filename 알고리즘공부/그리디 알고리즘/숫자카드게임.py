# 행과 열 입력받기
N, M = map(int, input().split())

result = 0
# 한 줄씩 입력받아서 확인
for i in range(N):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)

    # '가장 큰수' 고르기
    result = max(result, min_value)

print(result)