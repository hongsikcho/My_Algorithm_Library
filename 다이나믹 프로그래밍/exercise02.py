# 개미 전사 문제 
# 이또한 다이나믹 프로그래밍을 떠올리지 못하여 내 스스로 작성해보았다.
# 내코드

n = int(input())
list = list(map(int,input().split()))

sum1 = 0
sum2 = 0

for i in list:
    if i % 2 == 0:
        sum1 += i
    else:
        sum2 += i 

if sum1 >= sum2 :
    print(sum1)

if sum2 >= sum1 :
    print(sum2)
    
  
# 모범 답안
x = int(input())
array = list(map(int, input().split()))

d = [0] * 101
d[0] = array[0]
d[1] = max(array[0] , array[1])

for i in range(2 , n):
  d[i] = max(d[i - 1] , d[i - 2] + array[i])
  
print(d[x])

# 앞에 문제보다는 비교적 쉽게 느껴졌다.
# 역시나 DP테이블을 초기화하는게 중요하다고 생각된다.
# 보텀업방식 또한 계속해서 문제를 풀어나가면 익숙해질것같다.
