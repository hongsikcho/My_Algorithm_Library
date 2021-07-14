# 1로 만들기 문제.
# 사실 다이나믹 프로그래밍의 방식은 알았지만 처음 문제를 접했을때 어떻게 떠올려야 할지 감이 잡히지 않았다. 결국 그냥 내 생각대로 코딩을해서
# 답을 작성하긴 하였다.

# 내 풀이
n = int(input())

a = 1
total = 0
da = 0

while True:
    da = a * 5
    if da >= n :
        break
    a = da
    total += 1

while True:
    da = a * 3
    if da >= n:
        break
    a = da
    total += 1

while True:
    da = a * 2
    if da >= n:
        break
    a = da
    total += 1

while True:
    da = a + 1
    if da == n:
        a = da
        total += 1
        break
    else:
        a = da
        total += 1

print(total)

# 모범 답안

x = int(input())

d = [0] * 30001

for i in range(2 , x + 1):
  d[i] = d[i - 1] + 1
  
  if x % 2 == 0 :
    d[i] = min(d[i] , d[i] // 2 + 1)
  if x % 3 == 0 :
    d[i] = min(d[i] , d[i] // 3 + 1)
  if x % 5 == 0 :
    d[i] = min(d[i] , d[i] // 5 + 1)
print(d[x])

# x값이 정해짐에따라 함수가 호출되는 과정을 볼 때, 같은 함수가 여러번 나오고 쪼갤 수 있고 일반 그리디 문제로 접근했을 때와 문제가 사뭇 다르기 때문에 다이나믹 프로그래밍을 떠올린다.
# 점화식을 작성해 볼 생각을 떠올린다.
# 연습 많이 해야하는 유형
