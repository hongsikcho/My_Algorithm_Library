def solution(num):
    cnt = 0
    if num == 1:
        return 0
    while 1:
        if num%2 == 0:
            num //= 2
            cnt += 1
        elif num%2 != 0:
            num = num*3 + 1
            cnt += 1
            
        if num == 1:
            break
    if cnt > 500:
        return -1
    else:
        return cnt
