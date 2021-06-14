N = int(input())
stack = []
order = []
for i in range(N):
    order.append(str(input()))
    
for k in order:
    if k[:4] == 'push':
        stack.append(k[5:])
    elif k == 'top':
        if len(stack) < 1:
            print(-1)
        else:
            print(stack[-1])
    elif k == 'size':
        print(len(stack))
    elif k == 'pop':
        if len(stack) < 1:
            print(-1)
        else:
            s = stack[-1]
            stack.pop()
            print(s)
    elif k == 'empty':
        if len(stack) < 1:
            print(1)
        else:
            print(0)