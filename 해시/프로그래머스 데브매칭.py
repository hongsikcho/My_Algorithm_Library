def solution(lottos, win_nums):
    answer = []
    result = 0
    for i in lottos:
        if i in win_nums:
            result += 1

    high = result + lottos.count(0)
    low = result

    if high >= 2:
        answer.append(7 - high)
    else:
        answer.append(6)

    if low >= 2:
        answer.append(7 - low)
    else:
        answer.append(6)


    return answer
  
  # 문제에서 시키는대로 구현하면 됐음
  # 다른 사람의 풀이를 보니 배열을 생성해서 풀었는데 굉장히 좋은 방법이옸음
  # 인덱스 별로 correct = [6,6,5,4,3,2,1]  -> 깔끔한 풀이
