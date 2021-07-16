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
      
 # 이처럼 간단하게 구현한 다익스트라 알고리즘은 노드의 개수가 적을 때는 상관없지만 노드의 개수가 10,000개 이상으로 많아지면 시간복잡도가 올라가 시간초과 판정을 받을 수 있다.
 # 따라서 조금 더 개선된 다익스트라 알고리즘을 이용해야 하는데 여기서 사용되는게 '힙'이라는 개념이다.(자바로 따지면 스택,큐,우선순위 큐 이다.)
 # 힙 라이브러리에 사용 예제를 보면


 # 1.오름차순 정렬
 # 파이썬의 힙은 기본적으로 push하면 오름차순으로 정렬되도록 구현되어있음.
import heapq

def heapq(iterable):
  h = []
  result = []
  
  for value in iterable:
    heapq.heappush(h , value)
    
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2,4 ,6, 8, 0])
print(result)

==> 0,1,2,3,4,5,6,7,8,9

# 2.내림차순 정렬
import heapq

def heapq(iterable):
  h = []
  result = []
  
  for value in iterable:
    heapq.heappush(h , -value)
    
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2,4 ,6, 8, 0])
print(result)

==> 9,8,7,6,5,4,3,2,1

# 이러한 힙 라이브러리를 이용한 개선된 다익스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))


def dijkstra(start):
  q = []
  
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now heapq.heappop(q)
    
    if distance[now] < dist:
      continue
      
    for i in graph[now]:
      cost = dist + i[1]
      
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
        
 dijkstra(start)

for i in range(1 , n + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
