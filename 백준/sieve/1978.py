n = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in num:
    count = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        cnt += 1
print(cnt)