from itertools import combinations
import sys
from typing import List


n, m = map(int, input().split())
city = []
chicken = []
home = []
ans = 10e9

for _ in range(n):
    city.append(list(map(int, input().split())))


for i in range(n): ##치킨집과 일반집을 구분해서 저장
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            home.append([i, j])

chicks = combinations(chicken, m)#치킨집중 주어진 개수만큼 순서없이 뽑음


def dfs(chick):
    rs = 0
    global ans
    for h in home:
        dist = 10e9
        for c in chick:
            dist = min(dist, abs(h[0]-c[0])+abs(h[1]-c[1])) #거리 계산 시 이차원배열에서 각각의 인덱스의 차이로 구함(이런 경우 많은 듯)

        rs += dist

    ans = min(ans, rs)


for c in chicks:
    dfs(c)

print(ans)
