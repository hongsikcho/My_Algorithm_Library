def solution(arr):
    answer = []
    for a in arr:
        if [a] == answer[-1:]:
            continue
        answer.append(a)
    return answer
  
  
# 배열에서 [-1]을 리턴하면 배열 형태로 나옴
# 따라서 그냥 a와 비교하면 에러 남!
# 또한 처음 answer는 빈 배열이기 때문에 answer[-1] 말고  answer[-1:]로 새로운 배열을 만들어서 비교해야 함
