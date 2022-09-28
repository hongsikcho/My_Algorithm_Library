def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

#join함수는 반드시 이터레이터에서 사용! 또한 이터레이터 구성요소가 문자여야 가능 ! 숫자는 에러남

