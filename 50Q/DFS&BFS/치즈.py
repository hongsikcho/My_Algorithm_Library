from collections import deque


n , m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))


dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    visit = [[-1]*m for i in range(n)]
    q = deque()
    q.append([0,0])
    visit[0][0] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == -1: #방문하지 않은 곳이라면
                    if graph[nx][ny] >= 1: # 방문한곳이 치즈라면
                        graph[nx][ny] += 1 # 벽에 닿았으므로 + 1
                    else:
                        visit[nx][ny] = 0 # 방문한곳이 외부공기라면
                        q.append([nx,ny]) # 큐에 넣는다
                        # 이렇게 할 경우 안쪽 공기는 큐에 들어가지 않기 때문에 계산할 필요가 없어진다.

res = 0
while True:
    bfs()
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:  #외부공기에 닿은 수가 2번 이상일 경우
                cnt = 1
                graph[i][j] = 0
            elif graph[i][j] == 2: # 외부공기에 닿은 수가 1번일경우 사라지지않으므로 원래 상태로 되돌린다.
                graph[i][j] = 1
            
    if cnt == 1:
        res += 1
    else:
        break

print(res)

# bfs나 dfs에서는 방문여부를 체크하기 위해 새로운 배열을 만든다.
# 이 점을 항상 생각해두고 문제풀이 해볼 것 !
