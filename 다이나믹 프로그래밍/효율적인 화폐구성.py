n , m = map(int,input().split())

array = []

for i in range(n):
  array.append(i)
  
d = [999999] * (n+1)
d[0] = 0
for a in array:
  for i in range(a,n+1):
    if d[i-a] != 999999:
      d[a] = min(d[a] , d[i-a] + 1)
      

if d[m] != 999999:
  print(d[m])
else:
  print(-1)
  

  
#dp는 항사 처음 초기화된 것둘에게 힌트를 얻는 것 같음
#2원이 있을 때 a원을 만들고 싶으며 a-2원이 존재해야 한다.
 
