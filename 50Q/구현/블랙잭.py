n, m = map(int, input().split())

cards = list(map(int, input().split()))

cards.sort(reverse=True)

result = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cards[i]+cards[j]+cards[k] <= m:
                result = max(result, cards[i]+cards[j]+cards[k])


print(result)

# 카드가 주어지는 범위는 3 <= N <= 100
# 따라서 3중반복문을 사용해도 최대 1000000만번 연산하기 때문에 브루트포스를 사용할 수 있었음.
