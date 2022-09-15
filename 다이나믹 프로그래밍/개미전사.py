n = int(input())
array = list(map(int,input().split())))
d = [0] * 1000
d[0] = array[0]
d[1] = max(array[0] , array[1])


for i in range(2,n):
  d[i] = max(d[i-1] , d[i-2] +array[i])
  
print(d[n-1])

# d[n] = max(d[n-1] , d[n-2] + array[n]) 점화식 !! 
#dp는 점화식 생각하기가 어려움 , 하나하나 해보면서 할것
#그래프로 주어지며 그래프 자체를 dp테이블로, 아니라면 새로우 dp테이블 만들어서 사용
