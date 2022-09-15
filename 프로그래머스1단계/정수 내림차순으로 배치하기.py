def solution(n):
    n = sorted(str(n),reverse=True)
    
    ans = ''
    return int("".join(n)) 
 
#처음에느 다르 방식으로 해결했지만 join을 사용한 풀이가 더 깔끔함.
# "구분자".join으로 쓰인다.
# 예를 들어 "".join(리스트) -- >. ".".join([1,2,3,4,5])
# 출력값 = "1.2.3.4.5"



#문자열에서는 sort()함수가 존재하지 않고 sorted()함수마 존재한다.
#또한 sorted()함수르 사용하였을때 결과느 리스트로 반환된다.
# 대문자 < 소문자 < 순서 == > Aabc순으로 정렬
