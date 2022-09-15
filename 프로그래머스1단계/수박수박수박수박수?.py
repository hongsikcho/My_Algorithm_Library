def solution(n):
    a = '수박'
    if n % 2 == 0:
        a *= n//2
        return a
    else:
        a *= (n+1)//2
        return a[0:-1]
      
#짝수일때느 그냥 수박수박 홀수일때는 수박수박에서 박빼버려
