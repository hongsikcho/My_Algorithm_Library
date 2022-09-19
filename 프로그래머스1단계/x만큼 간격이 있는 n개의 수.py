def solution(x, n):
    answer = [x]
    cnt = x
    for i in range(n-1):
        cnt += x
        answer.append(cnt)
    return answer
