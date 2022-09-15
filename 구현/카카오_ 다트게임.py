def solution(dart):
    n = ''
    score = []
    for d in dart:
        if d.isnumeric():
            n += d
        elif d =='S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif d =='D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif d =='T':
            n = int(n)**3
            score.append(n)
            n = ''
        elif d == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif d =='#':
            score[-1] *= -1
    return sum(score)

#그냥 문제에서 시키는대로 하면 된다
#다만 숫자르 받을 때 여러자리 수 일 수 있으므로 계속해서 더해준 다음 숫자로 변환한다
#isalpha() : 주어진 문자열이 문자로만 이루어져 있는지
#isdigit() : 주어진 문자열이 숫자로만 이루어져 있는지
#upper(), lower(), isupper(), islower()등 문자에 관한 함수
#문자열은 sort()함수느 없고 sorted()함수마 존재한다. 대문자가 더 크고 뒤로 갈수록 수 더 크다.
