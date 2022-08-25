def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)
  ##마지막 정렬하여 답을 구하는 부분에서 막혔다. 이부분은 블로그에 따로 정리해두었다.
