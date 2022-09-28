def solution(n):
    
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return sieve[1:].count(True)-1
  
  #소수 찾는 함수는 잘 알아둘 것
  #에라토스테네스의 체
