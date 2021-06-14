N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort(reverse=True)
answer=0

for i in range(N):
  answer += A[i]*B[i]

print(answer)