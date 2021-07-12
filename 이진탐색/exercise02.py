# 문제 풀지 못하였음. 이진탐색으로 구현하는 것은 알았지만 문제를 제대로 이해하지 못하여서 조건을 너무 많이 나눈 것 같다.
# 나는 떡의길이가 최대가 되도록하는 절단기의 길이를 구하는 줄 알았다.

# 모범 답안 :

n, m = list(map(int,input().split(' ')))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0 

while start <= end :
  total = 0
  mid = (start + end) // 2
  
  for x in array:
    if x > mid:
      total = x - mid
      
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
    
    
print(result)

# 일단 탐색할 수가 많으면 항상 이진탐색을 고려한다.
    
