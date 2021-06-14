N = int(input())
num_list = []

for i in range(N):
    x, y = map(int, input().split())
    num_list.append((x, y))

num_list.sort(key = lambda num: (num[0], num[1]))

for num in num_list:
    print(num[0], num[1])