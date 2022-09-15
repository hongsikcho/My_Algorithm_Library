def solution(new_id):
    #1번 - 모든 문자를 소문자로 바꾼다
    new_id = new_id.lower()

    #2번 - 가능하 문자마 받아서 새로운 문자열을 구성함
    confirm = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i =='-' or i =='_' or i =='.':
            confirm+=i

    #3번 - '.'이 연속으로 들어온다며 하나만 사용
    confirm2 = '1'
    for i in confirm:
        if i =='.':
            if confirm2[-1] =='.':
                continue
        confirm2+=(i)
    
    #4번 - 맨앞, 맨뒤에 '.'이 들어온다며 제거..하지만 현재 문자열; '.'하나만 있을경우 a추가
    confirm = confirm2[1:]
    print(confirm)
    if confirm[0] == '.':
        confirm = confirm[1:]
    if len(confirm) == 0:
        confirm += 'a'
    if confirm[-1] == '.':
        confirm = confirm[0:-1]
    
    #5번 총 아이디 길이가 16이상이며 15까지 자름
    if len(confirm) >= 16:
        confirm = confirm[0:15]
        if confirm[-1] =='.':
            confirm = confirm[0:-1]
    
    #6번 - 총 길이가 2 이하이면 3이 될때까지 맨뒤 문자를 더해줌
    if len(confirm) <= 2 :
        while len(confirm) != 3:
            confirm += confirm[-1]
            
    return confirm
