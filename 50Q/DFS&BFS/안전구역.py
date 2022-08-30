import sys
sys.setrecursionlimit(10**6)
import copy


n = int(input())
high = 0
array = []
for _ in range(n):
    li = list(map(int, input().split()))
    high = max(high, max(li)) #제일 높은값을 구해야하기 때문에 받을 때 계산
    array.append(li)


def dfs(x, y, h, arrays):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if arrays[x][y] >= h:
        arrays[x][y] = 0
        dfs(x+1, y, h, arrays)
        dfs(x, y+1, h, arrays)
        dfs(x, y-1, h, arrays)
        dfs(x-1, y, h, arrays)
        return True

    return False


result = 0
for h in range(1, high+1):
    cnt = 0
    arrays = copy.deepcopy(array) #할때마다 새로운 배열이 필요하기때문에 copy사용
    for i in range(n):
        for j in range(n):
            if dfs(i, j, h, arrays) == True:
                cnt += 1

    result = max(result, cnt)

print(result)
