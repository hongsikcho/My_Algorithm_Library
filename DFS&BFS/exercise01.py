n ,m = map(int,input().split())

array = []

for i in range(n):
  array.append(list(map(int,input())))
  

def dfs(x,y):
  
  
  if x < 0 or y < 0 or x >=n or y >=n:
    return False
  
  if array[x][y] == 0:
    array[x][y] = 1
    
    dfs(x + 1 , y)
    dfs(x - 1 , y)
    dfs(x , y + 1)
    dfs(x , y - 1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1
      
print(result)

#입력받은 예시들을 저장
#2차원 배열 설정 시  (5~6)행은 자주 사용해야하므로 반드시 기억
#문제를 보고 붙어있는 부분을 어떻게 추려낼 수 있을까 생각
#바로 하려하지말고 함수로 만들어서 사용할 생각
