def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer


#split()과 spilt(" ")은 차이가 있다.
#전자는 공백 여러개를 하나로 취급, 후자는 공백이 여러개여도 하나만 공백으로 
=====다른 풀이=====
def solution(s):
    answer = ''
    s = s.split(" ")
    
    for a in s:
        
        if a =='': #공백 처리를 잘 해줄 것!
            answer += ' '
            continue
            
        b = a.lower()
        if a[0].isalpha():
            answer += (b[0].upper() +b[1:])
            answer+=' '
        else:
            answer += b
            answer += ' '
            
    
    return answer[:-1]
