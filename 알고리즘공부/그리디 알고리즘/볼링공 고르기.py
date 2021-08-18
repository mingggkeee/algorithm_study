n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0
for i in range(len(array)):
    temp = array[i]
    for j in range(i, len(array)):
        if temp == array[j]:
            continue
        else:
            result += 1

print(result)