# 문자열 s
s = input()

result1 = 0
result2 = 0
swap = 0
for i in s:
    if swap == 0:
        if swap == int(i):
            continue
        elif swap != int(i):
            result1 += 1
            swap = int(i)

    if swap == 1:
        if swap == int(i):
            continue
        else:
            result2 += 1
            swap = int(i)

result = min(result1, result2)

print(result)