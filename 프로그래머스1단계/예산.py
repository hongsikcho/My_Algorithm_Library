def solution(d, budget):
    answer = 0
    cnt = 0
    for b in sorted(d):
        if budget >= b:
            budget -= b
            cnt += 1
        else:
            break
    return cnt
