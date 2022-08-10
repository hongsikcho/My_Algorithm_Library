s = "abcabcdede"

result = len(s)

for i in range(1, len(s)//2+1): # 짝수일때 정확히 2등분, 홀수일때 하나 빠지지만 괜찮음
    gap = i
    last = s[0:gap]
    count = 1
    conn = ""
    for j in range(gap, len(s), gap): # 반복문에서는 len(s) -1 까지만 돌아가는것을 명심 !
        if s[j:j+gap] == last:
            count += 1
            continue
        else:
            if count >= 2:
                conn += str(count) + last
            else:
                conn += last
            last = s[j:j+gap]
            count = 1

    if count >= 2:
        conn += str(count) + last
    else:
        conn += last
    result = min(result, len(conn))

print(result)

#조금 더 신경써야 할 부분
#문자열에서 범위를 초과하여 출력하면 최대범위까지만 출력된다. ex) s="abcde" -> print(s[0:100]) -> abcde 출력
#for문에서 범위가 0 ~ n까지일때 항상 n-1번째까지 반복됨을 잊지말것
