r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = set()
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0


def dfs(x, y, cnt):
    global ans

    ans = max(ans, cnt)
    visited.add(graph[x][y])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] not in visited:
                dfs(nx, ny, cnt + 1)

    visited.remove(graph[x][y]) #완전탐색 진행 시 더이상 나아갈곳이 없으면 뒤로돌아와서 다른 탐색을 진행한다. 따라서 뒤로올때는 제일 최근에 밟은 알파벳은 제거해주어야한다.


dfs(0, 0, 1)

print(ans)
