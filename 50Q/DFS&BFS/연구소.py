import copy
from itertools import combinations
import sys
from collections import deque
n , m = map(int,input().split())
graph = []
possi = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            possi.append([i,j]) # 벽을 세울 수 있는 0인 공간을 새로운 배열에 추가
dx = [ -1,0,1,0]
dy = [0,-1,0,1]

answer = 0
def bfs(x,y): #바이러스를 퍼트리는 함수 bfs
    q = deque()
    q.append([x,y])
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if graph1[nx][ny] == 0:
                    graph1[nx][ny] = 2
                    q.append([nx,ny])
    

for p in list(combinations(possi,3)): #위에서 벽을 세울수 있는 공간을 담은 배열에서 순서 상관없이 3개씩 뽑음
    graph1 = copy.deepcopy(graph) # 원배열을 훼손하지 않도록 복사해서 사용
    for i in p:
        graph1[i[0]][i[1]] = 1 #벽 세움

    for i in range(n):
        for j in range(m):
            if graph1[i][j] == 2: #바이러스 퍼뜨림
                bfs(i,j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph1[i][j] == 0:
                cnt += 1 # 안전한 구역 개수 세기
                
    answer = max(answer,cnt) # 안전한구역의 개수의 최대값 구하기


print(answer)
