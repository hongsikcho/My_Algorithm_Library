# 선택 정렬
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다
# 기본 정렬 라이브러리를 포함해 다른 정렬 알고리즘과 비교했을 때 매우 비효율적이긴하다. 하지만 특정 리스트에서 가장 작은 데이터를 찾는 일이 코딩 테스트에서 잦으므로
# 익숙해질 필요가 있는 알고리즘.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1 , len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프 : 파이썬에서는 다른 라이브러리를 사용하지 않고 간단하게 표현가능
  
 print(array)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# 삽입 정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
# 선택정렬보다 효율적이다.
# 두 번째 데이터부터 시작한다. 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단하기때문이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
  
for i in range(1, len(array)):
  for j in range(i , 0 , -1): #인덱스 i부터 1까지 1씩감소하는 문법
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else:
      break
      
print(array)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다
# 일반적인 상황에서 가장 많이 사용되는 알고리즘
# 병합 정렬과 더불어 정렬 라이브러리의 근간이 되는 알고리즘
# 가장 기본적인 퀵 정렬에서는 첫 번째 데이터를 기준 데이터(Pivot)으로 설정한다
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    
    while left <= end and array[left] <= array[pivot]:
          left += 1
      
    while right > start and array[right] >= array[pivot]:
          right -= 1
        
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
      
  quick_sort(array, start, right -1)
  quick_sort(array, right+1 , end)
  
quick_sort(array, 0 , len(array) -1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬 소스코드----------------------------------------------------------------------------

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  
  pivot = array[0] # 피벗은 첫 번째 원소
  tail = array[1:] # 피벗을 제외한 리스트
  
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# 계수 정렬
# 특정한 조거이 부합할 때 매우 빠르게 동작하는 정렬 알고리즘
# 동일한 값을 가지는 데이터가 여러개 존재할 때 효율적이다

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1 )

for i in range(len(array)):
  count[array[i]] += 1
  
 for i in range(len(count)):
  for j in range(count[i]):
    print(i , end = " ")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    
