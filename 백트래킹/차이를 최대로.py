# 파이썬 순열 라이브러리 사용, 아이디어를 통한 구현으로 풀었는데 백트래킹 풀이도 있어서 작성해봄

def solution(pick, nums):
    global answer # 결과 값으로 사용할 answer변수
    if len(pick) == n: # 순서를 정하고 길이가 n이 되었을 때
        result = 0
        for i in range(n-1):
            result += abs(nums[pick[i]] - nums[pick[i+1]])
        answer = max(result, answer)
        return # 배열의 길이가 n 이 되고 한번의 결과도출이 실행되면 15line으로 이동
    for i in range(n): # 아직 배열의 길이가 n이 되지 않았다면
        if not visited[i]:
            visited[i] = 1 # 방문처리
            pick.append(i) # pick배열에 추가
            solution(pick, nums)
            visited[i] = 0 # 제일 마지막에 들어간 수 방문 x 처리
            pick.pop() # 제일 마지막에 들어간 수 빼기


n = int(input())
nums = list(map(int, input().split()))

visited = [0]*n
answer = 0
solution([], nums)
print(answer)
