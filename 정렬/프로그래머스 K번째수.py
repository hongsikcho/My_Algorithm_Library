def solution(array, commands):
    answer = []
    for c in commands:
        start = c[0] # 첫번째 값은 시작점
        end = c[1] # 두번째 값은 끝점
        idx = c[2] # 세번째 값은 찾고싶은 인덱스

        result = sorted(array[start - 1: end])
        answer.append(result[idx-1])
    return answer
  
  # 문자열 자르기
  # s[0:5] ==> 문자열 s에서 0번째 인덱스부터 4번째 인덱스까지 슬라이싱
  # 왼쪽에서 오른쪽으로만 진행
