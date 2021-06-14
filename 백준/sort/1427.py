num = int(input())

temp = str(num)
nums = []
for k in temp:
    nums.append(k)
nums.sort(reverse=True)
temp2 = ""
for i in nums:
    temp2 += i
num = int(temp2)
print(num)