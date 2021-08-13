# 정수 n 
n = int(input())

# 식량 정보 입력
array = list(map(int, input().split()))

d = [0] * 100

# dp 보텀업
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])