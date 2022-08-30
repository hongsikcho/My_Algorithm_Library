import sys
sys.setrecursionlimit(10**9)
n = int(input())
array = []
col = 0
ncol = 0
for i in range(n):
    array.append(list(map(str, input())))

color = [[0]*n for i in range(n)]
ncolor = [[0]*n for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def cdfs(x, y):
    color[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if array[x][y] == array[nx][ny] and color[nx][ny] == 0:
                cdfs(nx, ny)


def ndfs(x, y):
    ncolor[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if array[x][y] == array[nx][ny] and ncolor[nx][ny] == 0:
                ndfs(nx, ny)


for i in range(n):
    for j in range(n):
        if color[i][j] == 0:
            cdfs(i, j)
            col += 1


for i in range(n):
    for j in range(n):
        if array[i][j] == 'G':
            array[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if ncolor[i][j] == 0:
            ndfs(i, j)
            ncol += 1

print(col, ncol)
# 첫번째로 색맹이 아닌경우 먼저 계산
# 그리고 R과G를 같은것으로 보도록 변경
# DFS실행 시 굳이 주어진 배열을 바꾸지않아도 된다. 때에 따라서는 visited라는 방문배열을 생성하여 사용하자
