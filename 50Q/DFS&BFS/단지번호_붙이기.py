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
