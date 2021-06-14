from collections import deque

N = int(input())
order = []
queue = deque()
for i in range(N):
    order.append(str(input()))
    
for k in order:
    if k[:4] == 'push':
        queue.append(k[5:])
    elif k == 'front':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[0])
    elif k == 'back':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[-1])
    elif k == 'size':
        print(len(queue))
    elif k == 'pop':
        if len(queue) < 1:
            print(-1)
        else:
            s = queue[0]
            queue.popleft()
            print(s)
    elif k == 'empty':
        if len(queue) < 1:
            print(1)
        else:
            print(0)