def solution(n):
    if n == 1 or n == 2:
        return 1
    answer = 0
    for i in range((n//2)+1,0,-1):
        rs = 0
        for j in range(i,0,-1):
            rs += j
            if rs > n:
                break
            if rs == n:
                answer += 1
                break
        if rs < n:
            break
                        
            
        
    return answer+1
  
#처음에 정담을 맞췄지만 효율성에서 틀렸더 문제
#조건문을 잘 생각해볼 것
