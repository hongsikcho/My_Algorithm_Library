from collections import deque
n = int(input())
graph = []
rs = 10e9
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
cnt = 2

def bfs(x,y): #처음 섬 별로 다른 숫자로 세팅
    global cnt
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = cnt
                    q.append([nx,ny])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = cnt
            bfs(i,j)
            cnt += 1



def find(num): # chk 배열을 두어서 새로운 섬을 찾아갈때깢 bfs로 탐색
    chk = [[-1]*n for i in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                q.append((i,j))
                chk[i][j] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if graph[nx][ny] == 0 and chk[nx][ny] == -1:
                    chk[nx][ny] = chk[x][y] + 1
                    q.append([nx,ny])
                elif graph[nx][ny] > 0 and graph[nx][ny] != num:
                    return chk[x][y]

for k in range(2,cnt):
    a = find(k)
    rs = min(rs,a)
    


print(rs)
