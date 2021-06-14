N = int(input())
k = list(map(int, input().split()))
k.sort()
answer = 0
temp = 0
for l in k:
    temp += l
    answer += temp
print(answer)