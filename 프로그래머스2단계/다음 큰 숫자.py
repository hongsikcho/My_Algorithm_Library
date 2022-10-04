def solution(n):
    answer = 0
    cnt = n+1
    while 1:
        bcnt = list(bin(cnt)[2:])
        bn = list(bin(n)[2:])
        
        if bcnt.count('1') == bn.count('1'):
            break
        
        cnt += 1
    return cnt
  
#문제가 하라는대로마 하며 풀리는 문제
