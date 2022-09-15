n = int(input())

d = [0]*(n+1)
d[0] = 0
d[1] = 0
for i in range(2,n+1):
  #1으 빼줄 때
  d[i] = d[i-1] + 1
  
  if i%2 == 0 :
    d[i] = min(d[i] , d[i//2] + 1)
    
  elif i%3 == 0:
    d[i] == min(d[i] , d[i//3] + 1)
    
  elif i%5 == 0:
    d[i] == min(d[i] , d[i//3] + 1)
    
 print(d[n])

#보텀업 방식으로 생각해라
#작은것부터 하나하나씩 쌓아올린다느 느낌으로
#마지노선을 더하는 것 , 그 전에 나눌 수 있는 숫자가 있으면 그 d에 + 1 값
