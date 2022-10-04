def solution(n,a,b):
    answer = 0

    while 1 :
        answer += 1
        if a%2 == 0:
            a = a//2
        else:
            a = (a//2) + 1
            
        if b % 2 == 0:
            b //= 2
        else:
            b = (b//2) + 1
            
        if a == b:
            return answer 

#처음에 어려운 문제인 줄 알고 쫄았음
#토너먼트이므로 한 라운드가 끝나면 1/2가 탈락하기 때문에 번호도 1/2배로 당겨진다.
