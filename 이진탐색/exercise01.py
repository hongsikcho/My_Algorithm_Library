# 이 문제는 여러 방법으로 해결될 수 있다. 내 풀이 방법은 가장 간단하게 생각하여 집합 자료형을 사용하였다.
# 풀긴했지만 내가 생각한 풀이가 이것뿐이어서 이걸로 해결했을 뿐이다.
# 다양한 풀이법을 염두해두고 가장 효율적인 풀이가 어떤것인지 생각해 본 뒤 문제를 푸는 습관을 길러야겠다.

# 내풀이:
n = int(input())

my_list = list(map(int, input().split()))

m = int(input())

guest_list = list(map(int , input().split()))

for i in guest_list :
    if i in my_list :
        print("yes",end= ' ')
    else:
        print("no",end=' ')
        

# 이진탐색을 이용한 풀이 :

def binary_search(array, target, start, end):
  while start:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x :
  result = binary_search(array, i, 0 , n-1)
  if result != None:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')
    
 

#계수 정렬 푸이

n = int(input())
array = [0] * 1000001

for i in input().split():
  array[int(i)] = 1
  
  m = int(input())
  x = list(map(int, input().split()))
  
  for i in x :
    if array[i] == 1:
      print('yes' , end = ' ')
    else:
      print('no' , end = ' ')
