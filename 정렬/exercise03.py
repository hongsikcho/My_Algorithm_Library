# 입력을 받고 정렬 후 비교하면 되는 문제
# 내 코드 :
n , k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(map(int, input().split()))

for i in range(k):
    if a[i] < b[n-i-1]:
        a[i] = b[n-i-1]
    else:
        continue

sum = 0

for i in range(n):
    sum += a[i]


print(sum)

# 모범 답안
n, k = map(int , input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
  if a[i] <= b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break
    
 print(sum(a))

# 나는 두 배열 모두를 오름차순으로 정렬했고 모범답안에서는 a는 오름차순 , b는 내림차순으로 정렬하여 한번에 비교하였다.
# 차이는 없어보이지만 모범답안이 조금 더 깔끔한 코드인거같다.
# sum(a) == a리스트의 원소들의 합을 나타내는 메서드
