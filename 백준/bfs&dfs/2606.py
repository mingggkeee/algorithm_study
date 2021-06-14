computer = int(input())
network = int(input())
virus_map = [[0 for _ in range(computer + 1)] for _ in range(computer + 1)]

#2차원 배열 안에 넣어주기
for _ in range(network):
    x, y = map(int, input().split())
    virus_map[x][y] = 1
    virus_map[y][x] = 1


#1과 연결된 모든 노드 뽑기
def bfs(virus_map, start):
    queue = [start]
    visited = []
    
    while queue:
        temp = queue.pop(0)
        visited.append(temp)
        
        for i in range(len(virus_map)):
            if virus_map[temp][i] and i not in visited and i not in queue:
                queue.append(i)
                
    return len(visited) - 1


#1을 제외한 감염된 노드 수 출력
print(bfs(virus_map, 1))