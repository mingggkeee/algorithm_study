N = int(input())
weight = []

for i in range(N):
    weight.append(int(input()))

weight.sort()

weight2 = []

for i in range(N):
    count = N - i 
    weight_sum = weight[i] 
    weight2.append(weight_sum*count)

print(max(weight2))