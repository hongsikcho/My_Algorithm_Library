#dfs
nn = int(input())
graph = []
chk = [[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
rs = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = []

def dfs(x,y):
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx <n and 0 <= ny < n:
            if chk[nx][ny] == 0 and graph[nx][ny] == 1:
                chk[nx][ny] = 1
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if chk[i][j] == 0 and graph[i][j] == 1:
            chk[i][j] = 1
            cnt = 0
            dfs(i,j)
            answer.append(cnt)
            
print(len(answer))
for i in sorted(answer):
    print(i)
    
    
    
#bfs
n = int(input())
graph = []
chk = [[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
rs = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = []

def dfs(x,y):
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx <n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx,ny)
             


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            cnt = 0
            dfs(i,j)
            answer.append(cnt)
            
print(len(answer))
for i in sorted(answer):
    print(i)
