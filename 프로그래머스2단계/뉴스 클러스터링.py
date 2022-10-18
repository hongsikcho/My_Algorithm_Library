from collections import Counter
def solution(str1, str2): 

    # arr1: str1에 대한 문자쌍 배열
    # arr2: str2에 대한 문자쌍 배열
    arr1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    if len(arr1) == 0 and len(arr2) == 0:     # arr1 과 arr2가 공집합일경우
        return 65536

    c1 = Counter(arr1)
    c2 = Counter(arr2)
    
    sum_set = sum((c1 | c2).values())         # c1 과 c2 의 합집합
    inter_set = sum((c1 & c2).values())       # c1 과 c2 의 교집합

    return int(inter_set / sum_set * 65536)
  
#파이썬 Counter
#Counter(이터레이터)를 하면 각 요소가 몇개 존재하는지 key,value형태로 반환
#Counter([1,2,3]) == > Counter({1:1 , 2:1 , 3:1})
#교집합 차집합도 가능
#a | b , a & b ==> 합, 교
