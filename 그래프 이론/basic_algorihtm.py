# 서로소 집합 알고리즘 소스코드
def find_parent(parent , x):
  if parent[x] != x:
    return find(parent , parent[x])
  return x

def union_parent(parent, a, b):
  a = find_parent(parent , a)
  b = find_parent(parent , b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    

v, e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1 , v+1):
  parent[i] = i
  
  
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent , a, b)
  
 
print('각 원소가 속한 집합' , end = ' ')
for i in range(1 , v+1):
  print(find_parent(parent, i), end = ' ')
  
  
print()

print('부모 테이블:' , end = ' ')
for i in range(1 , v + 1):
  print(parent[i], end = ' ')
  
  
  
# 서로소 집합을 활용한 사이클 판별
# 서로소 집합은 다양한 알고리즘에 사용될 수 있다. 특히 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다는 특징이 있다. 참고로 방향 그래프에서의
# 사이클 여부는 DFS를 이용하여 판별할 수 있다.
# 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
# 2. 루트 노드가 서로 다르다면 두 노드에 대하여 UNION연산을 수행한다.
# 2. 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것이다.
# 3. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

# 서로소 집합을 활용한 사이클 판별 소스코드

def find_parent(parent , x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent ,a ,b):
  a = find_parent(parent , a)
  b = find_parent(parent , b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1 , v + 1):
  parent[i] = i
  
  cycle = False
  
  for i in range(e):
    a, b = map(int,input().split())
    if find_parent(parent , a) == find_parent(parent, b):
      cycle = True
      break
      
    else:
      union_parent(parent , a, b)
      
 

# 크루스칼 알고리즘이란 가장 적은 비용으로 모든 노드를 연결할 수 있는데 크루스칼 알고리즘은 그리디 알고리즘으로 분류된다. 먼저 모든 간선에 대햐여 정렬을 수행한 뒤어
# 가장 거리가 짧은 간선부터 집합에 포함시키면 된다. 이 때 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다.
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
# 2. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
# 2. 사이클이 발생한 경우 최소 신장 트리에 포함시키지 않는다.
# 3. 모든 간선에 대하여 2번의 과정들을 반복한다.

#크루스칼 알고리즘 소스코드

def find_parent(parent , x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent ,a ,b):
  a = find_parent(parent , a)
  b = find_parent(parent , b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
v, e = map(int, input().split())
parent = [0] * (v + 1)

result = 0
edges = []

for i in range(1 , v + 1):
  parent[i] = i
  
for _ in range(e):
  a, b, cost = map(int,input().split())
  edges.append((cost, a, b))
  
  edges.sort()
  
  for edge in edges:
    cost, a, b = edge
    if find_parent(parent , a ) != find_parent(parent, b):
      union_parent(parent, a, b)
      result += cost
      
  print(result)
  
  # 위상 정렬: 정렬 알고리즘의 일종이다. 위상 정렬은 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다. 조금 더 이론적으로 설명하자면 위상 정렬
  # 이란 방향 그래프의 모든 노드를 '방향성애 거스르지 않도록 순서대로 나열하는 것'이다.
  # 1. 진입차수가 0인 노드를 큐에 넣는다
  # 2. 큐가 빌 때까지 다음의 과정을 반복한다.
  # 3. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
  # 3. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
  
  from collections import deque
  
  v , e = map(int, input().split())
  
  indegree = [0] * (v + 1)
  graph = [[] for i in range(v + 1)]
  
  for _ in rnage(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
  def topology_sort():
    result = []
    q = deque()
    
    for i in range(1 , v+1):
      if indegree[i] == 0
      q.append(i)
      
    while q:
      new = q.popleft()
      result.append(now)
      
      for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
          q.append[i]
          
  for i in result:
    print(i , end= ' ')
    
  topology_sort()
