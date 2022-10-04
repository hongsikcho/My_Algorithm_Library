def solution(s):
    answer = []
    cnt = 0
    rs = 0
    while 1:
        rs += 1
        new_one = ''
        for i in s:
            if i == '0':
                cnt += 1
                continue
            new_one += i
        
        num = len(new_one)
    
        s = bin(num)[2:]
        
        if s == '1':
            break
        
        
    answer.append(rs)
    answer.append(cnt)
    return answer
  
  #문제가 하라는대로만 하면 풀렸더 문제
  #파이썬에서 이진수로 변환할때 bin(num)[2:]르 잊지말자
