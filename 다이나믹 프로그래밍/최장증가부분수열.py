n = int(input())
array = list(map(int,input().split()))

dp = [1]*n

for i in range(0,n):
  for j in rnage(0,i):
    if array[j] <= array[i]:
      d[i] =max(d[i] , d[j]+1)
      
print(n-max(dp))

#가장 기 증가하느 부분수열 (LIS)는 wellknown문제이므로 반드시 익힐 것 !
#디피에는 유명한 유형이 몇개 있다. 이 부분으 확실히 챙기고 갈 것!
      
      
