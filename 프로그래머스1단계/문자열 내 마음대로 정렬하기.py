def solution(strings, n):
    strings= sorted(strings, key = lambda x:(x[n],x))
    return strings
  
#lambda를 사용하여 첫번째 기준은 자신이 정한 인덱스 값으로 정렬
#두번째 기준은 기본 기준으로 정렬
