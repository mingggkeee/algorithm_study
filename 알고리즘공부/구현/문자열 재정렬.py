s = input()

result = []
count = 0

for i in s:
    if i.isdigit():
        count += int(i)
    else:
        result.append(i)
result.sort()
for i in result:
    print(i, end='')
print(count)