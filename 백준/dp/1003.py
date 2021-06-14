T = int(input())

c0 = [1,0,1]
c1 = [0,1,1]

def fibo(n):
    if len(c0) <= n:
        for i in range(len(c0), n+1):
            c0.append(c0[i-1] + c0[i-2])
            c1.append(c1[i-1] + c1[i-2])
    print(c0[n], c1[n])

for i in range(T):
    N = int(input())
    fibo(N)