from collections import deque

def solution(pri, location):
    
    pri = deque(pri)
    answer = 1
    wanted = pri[location]
    
    while 1:
        if pri[0] == max(pri):
            if pri[0] == wanted and location == 0:
                return answer
            pri.popleft()
            answer += 1
            if location == 0:
                location = len(pri)-1
            else:
                location -= 1
            
        else:
            pri.append(pri.popleft())
            if location == 0:
                location = len(pri)-1
            else:
                location -= 1
            
    return answer
