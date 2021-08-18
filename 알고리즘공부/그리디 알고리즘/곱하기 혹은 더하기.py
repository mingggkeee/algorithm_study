# 문자열 입력
s = input()

result = 0

for i in s:
    if i == '0':
        result += int(i)
    else:
        if result == 0:
            result += int(i)
        else:
            result *= int(i)

print(result)