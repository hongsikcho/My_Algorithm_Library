from collections import defaultdict

def solution(s):
    answer = []
    d = defaultdict(int)
    cnt = ''
    for i in s:
        if i.isdigit():
            cnt += i
            continue
        else:
            if cnt != '':
                d[int(cnt)] += 1
                cnt = ''
                
    array = sorted(d.items(),key = lambda x : -x[1])
    for i in array:
        answer.append(i[0])
    return answer
  

  
  
# defaultdict을 사용하여 해당 숫자가 얼마나 나오는지 저장
# 딕셔너리에 저장된 키,값을 불러와 값이 높은순으로 정렬
