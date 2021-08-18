# 모험가의 수 n
n = int(input())
# 각 모험가의 공포도 
people = list(map(int, input().split()))

people.sort()

result = 0

while True:
    if len(people) == 0:
        break
    elif len(people) >= people[-1]:
        sub = people[-1]
        for i in range(sub):
            people.pop()
        result += 1
    else:
        break

print(result)