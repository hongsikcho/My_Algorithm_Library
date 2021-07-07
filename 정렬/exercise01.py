# 정렬을 사용하는 기본적인 문제였다.

# 내 코드:

n = int(input())

list = []

for i in range(n):
    list.append(int(input()))

def my_sort():

    for i in range(len(list)):
        max_index = i
        for j in range(i+1 , len(list)):
            if list[max_index] <= list[j]:
                max_index = j
        list[max_index], list[i] = list[i], list[max_index]

    print(list)

my_sort()

# 모범 작성 코드:

n = int(input())

array = []

for i in range(n):
  array.append(int(input))
  
 
array = sorted(array, reverse = True)

for i in array:
  print(i , end = " ")
  
 # 파이썬에서는 리스트 정렬로 sort,sorted를 제공하므로 이 메서드 사용 시 더 빠르게 작성할 수 있음. 꼭기억!
 # sort()는 리스트의 원본을 변환시켜 저장. sorted()는 원본을 변환시키지않고 그때만 변환하여 다른 변수에 저장하는 메서드
