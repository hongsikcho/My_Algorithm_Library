n = int(input())
arrays = []
result = []
for _ in range(n):
    arrays.append(list(map(int, input())))


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if arrays[x][y] == 1:

        arrays[x][y] = 0
        cnt += 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j) == True:
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)n = int(input())
arrays = []
result = []
for _ in range(n):
    arrays.append(list(map(int, input())))


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if arrays[x][y] == 1:

        arrays[x][y] = 0
        cnt += 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j) == True:
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)
    
    
#dfs의 다른풀이

n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
