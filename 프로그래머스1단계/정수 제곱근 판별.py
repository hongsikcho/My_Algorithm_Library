def solution(n):
    if int(n**(1/2))**2 == n:
        return int((n**(1/2))+1)**2
    else:
        return -1
      
#제곱근이라면 제곱근을 구한뒤 다시 제곱했을때 해당하는 수가 나와야함
#파이썬에서 나누기느 a//b는 정수 반환 , a/b는 실수 반환
