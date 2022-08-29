def solution(s, n):
    basic = 'abcdefghijklmnopqrstuvwxyz' #알파벳을 모두 가진 문자열
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' ' # 공백일때 패스
            continue
        if i.isupper(): # 만약 대문자라면 소문자로 변경하기 위해 확인
            i = i.lower() # lower() , upper()함수는 리턴값 있으므로 반드시 저장해줘야함!! 이거때매 에러남
            b = basic.index(i)+n
            b %= 26 # 나누기로 해당 인덱스 찾아감
            answer += basic[b].upper()
        else:
            b = basic.index(i)+n
            b %= 26
            answer += basic[b]

    return answer
