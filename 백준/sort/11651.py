N = int(input())
num = []
for i in range(N):
  a, b = map(int, input().split())
  num.append((a,b))
num.sort(key=lambda x: (x[1], x[0]))
for i in num:
    print(i[0], end=' ')
    print(i[1])