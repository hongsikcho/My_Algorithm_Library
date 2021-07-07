# 튜플과 람다를 이용하여 정렬하는 쉬운 문제였지만 문법 공부의 부족함으로 풀지 못하였음

# 모범 답안 :
 
 n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  array.append((input_data[0] , int(input_data[1])))
  
  array = sorted(array , key = lamda student : studet[1]) # array의 2번째 요소들로 비교하여 정렬한다.
  
 
for student in array:
  print(student[0] , end = " ")
  
 # 리스트 정렬시 사용하는 lamda를 잘 기억하기.
 # lamda x : (len(X) , x) 처럼 여러 기준으로 비교할 수도 있다.
