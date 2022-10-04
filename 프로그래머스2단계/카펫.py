def solution(brown, yellow):
    answer = []
    check = []
    for i in range(1,yellow+1): ##노란색을 정확히 갈색이 한겹으로 둘러야하므로 yellow가 나누어 떨어지느 수로 층으로 나눈다.
        if yellow%i == 0:
            check.append(i)
    

    
    for c in check:
        side = (c*2)+4
        if side + (yellow//c)*2 ==brown: # 사실 가로가 더 길어야한다느 조건으 추가해주어야한다.
            answer.append([(yellow//c)+2,side//2]) 
            break
        
    return answer[0]
