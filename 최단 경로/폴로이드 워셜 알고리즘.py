# 다익스트라 알고리즘은 '한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우'에 사용할 수 있는 최단 경로 알고리즘이다.
# 플로이드 워셜 알고리즘은 '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우'에 사용할 수 있는 알고리즘이다.
# 단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택한다.
# 그렇게 모든 거리를 갱신해간다.
# 소스 코드:

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * [n + 1] for _ in range(n + 1)]

for a in range(1 , n+1):
  for b in range(1 , n+1):
    if a == b:
      graph[a][b] = 0
      
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c
  
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      
for a in range(1 , n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF :
      print("INFINITY", end = " ")
    else:
      print(graph[a][b] , end= " ")
  print()
