# 최단 경로를 구하기 위한 알고리즘으로 다익스트라 알고리즘이있다.
#다익스트라 알고리즘의 원리를 순서대로 설명하면 다음과 같다.
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3번과 4번을 반복한다.

# 다익스트라 알고리즘은 최단 경로를 구하는 과정에서 다이나믹 프로그래밍의 일종으로 볼 수 있고 위 4번 과정을 수행한다는 점에서 그리디 알고리즘으로도 볼 수 있다.
# 우선 간단한 다익스트라 알고리즘의 소스코드부터 적겠다.

import sys
input = sys.stdin.readline
INF = it(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]

visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  
 

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  
  for j in graph[start]:
    distance[j[0]] = j[i]
    
  for i in range(n - 1):
    now = get_smallest_node()
    visited[now] = True
    
  for j in graph[now]:
    cost = distance[now] + j[1]
    
    if cost < distance[j[0]]:
      distance[j[0]] = cost
      
  dijkstra(start)
  
  for i in range(1, n + 1):
    if distance[i] == INF:
      print("INFINITY")
    else:
      print(distance[i])
