def solution(s):
    answer = ''
    cnt = 1
    for i in s:
        if i == ' ':
            answer += i
            cnt = 1
            continue
        elif cnt%2 == 1:
            answer += i.upper()
        elif cnt%2 == 0:
            answer += i.lower()
        
        cnt += 1
            
    return answer
