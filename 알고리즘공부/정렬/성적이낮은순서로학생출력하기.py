# 학생수 입력
n = int(input())
# 학생 이름과 성적 입력
grade = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환해서 저장
    grade.append((input_data[0], int(input_data[1])))

grade.sort(key = lambda student: student[1])

for i in grade:
    print(i[0], end=' ')