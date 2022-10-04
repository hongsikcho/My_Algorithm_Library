def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
  
#문자열.split()과 문자열.split(" ")은 차이가 있다.
#전자는 모든 공백을 하나로 취급한다. 하지만 후자는 첫번째것만 공백으로 취급한다.
