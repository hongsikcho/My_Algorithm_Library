# 순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.

def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1
    
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요 : ")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n , target, array))

# 이진탐색 : 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
# 내부적으로 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  
  if array[mid] == target:
    return mid
  
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  
  else:
    return binary_search(array, target, mid + 1, end)
  
  n, target = list(map(int, input().split()))
  array = list(map(int, input().split()))
  
  result = binary_Search(array, target, 0 ,n - 1)
  if result == None:
    print("원소가 존재하지 않습니다")
  else:
    print(result + 1)
    
# 빠르게 입력받기 : 입력 데이터의 수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려서 시간 초과가 될 수 있다.
# 이럴때는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.

import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

# rstrip()은 줄바꿈을 제거하는 메서드
