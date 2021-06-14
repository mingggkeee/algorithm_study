from collections import deque

N = int(input())
order = []
queue = deque()
for i in range(N):
    order.append(str(input()))
    
for k in order:
    if k[:9] == 'push_back':
        queue.append(k[10:])
    elif k[:10] == 'push_front':
        queue.appendleft(k[11:])
    elif k == 'pop_front':
        if len(queue) < 1:
            print(-1)
        else:
            s = queue[0]
            queue.popleft()
            print(s)
    elif k == 'pop_back':
        if len(queue) < 1:
            print(-1)
        else:
            s = queue[-1]
            queue.pop()
            print(s)  
        
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
    elif k == 'empty':
        if len(queue) < 1:
            print(1)
        else:
            print(0)