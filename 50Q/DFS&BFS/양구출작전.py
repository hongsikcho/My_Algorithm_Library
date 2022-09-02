import sys
sys.setrecursionlimit(123458)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
node = [[], [0,0]]

# 1. 트리구조 만들기
for i in range(N-1):
    kind, number, connection = input().split()
    tree[int(connection)].append(i+2)
    node.append([kind, int(number)])


# 2. dfs를 이용하여 탐색하기
def dfs(v): # v : 현재 노드
    result = 0 

    # 노드들을 탐색하며 더해준다.
    for i in tree[v]:
        result += dfs(i)

    # 노드의 타입이 늑대라면 빼준다.
    if node[v][0] == 'W':
        result -= node[v][1]
        if result < 0:
            result = 0
    # 노드의 타입이 양이라면 더해준다.
    else:
        result += node[v][1]
    return result

print(dfs(1))

#dfs 이전에 로직을 두느냐 dfs 이후에 로직을 두느냐에 따라서 결과 호출이 달라짐
