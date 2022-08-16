# 서로 다른 n개의 수들 중 m개를 뽑아 일렬로 나열하는 경우의 수를 구하시오.
# for문을 계속 사용하기에는 n과 m이 정해지지 않아 불가능
# 파이썬의 내장 함수를 사용하기에는 날로먹는? 느낌
# 따라서 백트래킹 사용
n , m = map(int, input(),split())
nums = list(map(int,input().split())
answer = []
visited = [0] * n

def sol(pick , nums):
  global answer
  if len(pick) == m:
    result = []
    answer.append(pick)
    return
  
  for i in range(n):
    if i not visited:
      visited[i] = 1
      pick.append(nums[i])
      visited[i] = 0
      pick.pop()
    
